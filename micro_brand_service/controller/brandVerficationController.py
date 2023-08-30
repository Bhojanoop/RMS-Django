from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.logger.logging import log
from micro_brand_service.service.brand_verification_service.main import BrandVerifyMainService

import logging

logger=logging.getLogger('mylogger')

class BrandVerificationController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service=BrandVerifyMainService()

    @log(logger=logger)
    def post(self,request):
        res=self._service.verify(request=request)
        return Response(res,status=status.HTTP_202_ACCEPTED)
    
    @log(logger=logger)
    def get(self,request):
        res=self._service.getAll(request=request)
        return Response(res,status=status.HTTP_200_OK)
    
    
    