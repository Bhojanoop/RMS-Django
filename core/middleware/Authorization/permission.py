import json
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime
from micro_auth_service.jwt.main import JwtBuilder
import os

middleware_json=os.path.join(settings.BASE_DIR,'middleware.json')

class Authorization:
    def __init__(self, get_response):
        self.get_response = get_response
        with open(middleware_json, "r") as read_file:
            self._register_paths:dict=json.load(read_file)
    
    def get_exact_loc(self,request:object)->dict:
        incoming_req_path=str(request.path).split("/")
        all_registered_paths=self._register_paths['paths']
        for path in all_registered_paths:
            if path['endpoint'] in incoming_req_path:
                return path
    
    def hasToken(self,request):
        if request.META.get('HTTP_AUTHORIZATION'):
            return True
        else:
           return False
    
    def isTokenValid(self,request):
        try:
            res=JwtBuilder(token=(request.META.get('HTTP_AUTHORIZATION').split(' ', 1)[1])).decode()
            print(res)
            if res.get('sub'):
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def __call__(self, request):
        loc=self.get_exact_loc(request=request)
        if loc and loc['protected']==1:
            if not self.hasToken(request=request):
                return JsonResponse({'message': 'no bearer token found!',"timestamp":datetime.timestamp(datetime.now())}, status=403)
            elif not self.isTokenValid(request=request):
                return JsonResponse({'message': 'token is invalid!',"timestamp":datetime.timestamp(datetime.now())}, status=403)

        response = self.get_response(request)
        return response