from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from micro_branch_service.service.branch_main_service.main import BranchMainService
from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class BranchMainController(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self._service:BranchMainService=BranchMainService

    @log(logger=logger)
    def post(self,request):
        res=self._service().create(request=request)
        return Response(res,status=status.HTTP_201_CREATED)
    
    