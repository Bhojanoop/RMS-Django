from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status

from micro_brand_service.service.brand_creation_service.main import MainService

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class BrandCreateController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service:MainService=MainService()

    @log(logger=logger)
    def post(self,request):
        res=self._service.create(request=request)
        return Response(res,status=status.HTTP_201_CREATED)