from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from micro_auth_service.service.register.main import MainRegisterService

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class Register(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service:MainRegisterService=MainRegisterService()

    @log(logger=logger)
    def post(self,request:object,usertype:str):
        message=self._service.register(request=request,usertype=usertype)
        return Response(message,status=status.HTTP_201_CREATED)