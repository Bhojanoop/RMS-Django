from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class Login(APIView):

    def __init__(self, **kwargs: Any) -> None:
        pass

    @log(logger=logger)
    def post(self,request:object,usertype:str):
        message:dict
        return Response(message,status=status.HTTP_200_OK)