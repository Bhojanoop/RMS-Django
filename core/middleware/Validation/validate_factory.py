import json
from django.conf import settings
from core.middleware.Validation.micro_auth_service_login.main import LoginValidationMiddleware
from core.middleware.Validation.micro_auth_service_register.main import RegisterValidationMiddleware
from core.middleware.Validation.micro_auth_service_otpverify.main import OTPValidationMiddleware
from core.middleware.Validation.micro_auth_service_mailverify.main import MailVerifyValidationMiddleware


import os

middleware_json=os.path.join(settings.BASE_DIR,'middleware.json')

class Factory:

    def __init__(self) -> None:
        with open(middleware_json, "r") as read_file:
            self._register_paths:dict=json.load(read_file)
    
    def get_exact_loc(self,request:object)->dict:
        incoming_req_path=str(request.path).split("/")
        if incoming_req_path[1]!='admin':
            all_registered_paths=self._register_paths['paths']
            for path in all_registered_paths:
                if path['endpoint'] in incoming_req_path:
                    return path
            
    def middleware(self,request:object)->object:
        loc=self.get_exact_loc(request=request)
        if loc and loc.get("validation")==1: 
            if loc['endpoint']=='login' and loc['app']=='micro_auth_service':
                return LoginValidationMiddleware()
            elif loc['endpoint']=='register' and loc['app']=='micro_auth_service':
                return RegisterValidationMiddleware()
            elif loc['endpoint']=='otp-verification' and loc['app']=='micro_auth_service':
                return OTPValidationMiddleware()
            elif loc['endpoint']=='mail-verify' and loc['app']=='micro_auth_service':
                return MailVerifyValidationMiddleware()
  
        return None