from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

from micro_auth_service.service.login.main import MainLoginService

class Login(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._loginservice=MainLoginService()

    @log(logger=logger)
    def post(self,request:object,usertype:str):
        message=self._loginservice.login(request=request,usertype=usertype)
        return Response(message,status=status.HTTP_200_OK)