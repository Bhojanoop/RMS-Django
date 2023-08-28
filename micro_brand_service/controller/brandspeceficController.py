from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.logger.logging import log
from micro_brand_service.service.brand_specefic_service.main import BrandSpeceficService

import logging

logger=logging.getLogger('mylogger')

class BrandSpeceficController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service:BrandSpeceficService=BrandSpeceficService

    @log(logger=logger)
    def patch(self,request,brand_id):
        res=self._service().patch(request=request,brand_id=brand_id)
        return Response(res,status=status.HTTP_202_ACCEPTED)
    
    @log(logger=logger)
    def delete(self,request,brand_id):
        res=self._service().delete(brand_id=brand_id)
        return Response(res,status=status.HTTP_202_ACCEPTED)
    
    @log(logger=logger)
    def get(self,request,brand_id):
        res=self._service().get(brand_id=brand_id)
        return Response(res,status=status.HTTP_200_OK)
    