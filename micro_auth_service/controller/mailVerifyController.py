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
        self._service=MainMailVerifyService()

    def get(self,request,email,user):
        try:
            service=self._service.verify(email)
            if service:
                return render(request=request,template_name='email_verify.html',context={
                    "user":user
                })
            else:
                return render(request=request,template_name='page_not_found.html')
        except Exception as e:
            return render(request=request,template_name='page_not_found.html')

