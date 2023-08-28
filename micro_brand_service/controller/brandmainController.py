from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from micro_brand_service.service.brand_main_service.main import MainService

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class BrandMainController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service:MainService=MainService

    @log(logger=logger)
    def post(self,request,page=None):
        res=self._service().create(request=request)
        return Response(res,status=status.HTTP_201_CREATED)
    
    @log(logger=logger)
    def get(self,request,page=None):
        page=request.path.split("/")[len(request.path.split("/"))-1]
        res=self._service().getAll(int(page))
        return Response(res,status=status.HTTP_200_OK)
    