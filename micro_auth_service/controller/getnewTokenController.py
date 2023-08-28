from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from micro_auth_service.service.newtoken.main import NewTokenService

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class GetNewToken(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service:NewTokenService=NewTokenService

    @log(logger=logger)
    def get(self,request:object,usertype:str,userid:str):
        message=self._service().get(usertype=usertype,userid=userid,request=request)
        return Response(message,status=status.HTTP_201_CREATED)