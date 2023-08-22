from rest_framework.response import Response
from datetime import datetime
from rest_framework import status


def log(logger):
    def Inner(func):
        
        def wrapper(*args, **kwargs):
            package=func.__module__
            position=func.__qualname__
            try:
                logger.info(f"package : {package} --> position : {position}")
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"package : {package} --> position : {position} --> exception : {str(e)}")
                return Response({"message":str(e),"timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_400_BAD_REQUEST)
        return wrapper
    return Inner