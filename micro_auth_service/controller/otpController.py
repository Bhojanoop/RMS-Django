from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.logger.logging import log
from micro_auth_service.service.otp.main import MainOtpService

import logging

logger=logging.getLogger('mylogger')

class OtpController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service=MainOtpService

    @log(logger=logger)
    def post(self,request:object):
        message=self._service().process(request)
        return Response(message,status=status.HTTP_202_ACCEPTED)