from core.middleware.Validation.validate_factory import Factory
from django.http import JsonResponse
from datetime import datetime

class ValidateMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        try:
            ob=Factory().middleware(request=request)
            if ob:
                ob.validates(request=request)
           
            response = self.get_response(request)
            return response
        except Exception as e:
            return JsonResponse({'message': str(e),"timestamp":datetime.timestamp(datetime.now())}, status=400)