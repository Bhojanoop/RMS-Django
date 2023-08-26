from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from core.logger.logging import log
from micro_auth_service.service.mailverify.sent.main import MainMailSentService
from micro_auth_service.service.mailverify.verify.main import MainMailVerifyService

import logging

logger=logging.getLogger('mylogger')

class MailVerificationController(APIView):
    def __init__(self, **kwargs: Any) -> None:
        self._service=MainMailSentService

    @log(logger=logger)
    def post(self,request:object):
        message=self._service().send(request)
        return Response(message,status=status.HTTP_200_OK)

class MailVerify(View):
    def __init__(self, **kwargs: Any) -> None:
        self._service=MainMailVerifyService

    def get(self,request,email):
        try:
            service=self._service().verify(email)
            if service:
                return HttpResponse('<h1>Verified</h1>')
            else:
                return HttpResponse('<h1>not found</h1>')
        except Exception as e:
            return HttpResponse(f'<h1>{str(e)}</h1>')
