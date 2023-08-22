import json
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime

class Authorization:
    def __init__(self, get_response):
        self.get_response = get_response
        with open(f"{settings.BASE_DIR}\\middleware.json", "r") as read_file:
            self._register_paths:dict=json.load(read_file)
    
    def get_exact_loc(self,request:object)->dict:
        incoming_req_path=str(request.path).split("/")
        all_registered_paths=self._register_paths['paths']
        for path in all_registered_paths:
            if path['endpoint'] in incoming_req_path:
                return path
    
    def isAuthorized(self,request:object)->bool:
        if request.META.get('HTTP_X_USERID'):
            return True
        else:
           return False

    def __call__(self, request):
        loc=self.get_exact_loc(request=request)
        if loc and loc['protected']==1:
            if not self.isAuthorized(request=request):
                return JsonResponse({'message': 'permission denied!',"timestamp":datetime.timestamp(datetime.now())}, status=403)

        response = self.get_response(request)
        return response