from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status

from core.logger.logging import log

import logging

logger=logging.getLogger('mylogger')

class BrandCreateController(APIView):

    @log(logger=logger)
    def post(self,request):
        return Response()