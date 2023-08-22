import json
from django.conf import settings
from core.middleware.Validation.micro_auth_service_login.main import LoginValidationMiddleware
from core.middleware.Validation.micro_auth_service_register.main import RegisterValidationMiddleware

class Factory:

    def __init__(self) -> None:
        with open(f"{settings.BASE_DIR}\\middleware.json", "r") as read_file:
            self._register_paths:dict=json.load(read_file)
    
    def get_exact_loc(self,request:object)->dict:
        incoming_req_path=str(request.path).split("/")
        all_registered_paths=self._register_paths['paths']
        for path in all_registered_paths:
            if path['endpoint'] in incoming_req_path:
                return path
            
    def middleware(self,request:object)->object:
        loc=self.get_exact_loc(request=request)
        if loc: 
            if loc['endpoint']=='login' and loc['app']=='micro_auth_service':
                return LoginValidationMiddleware()
            elif loc['endpoint']=='register' and loc['app']=='micro_auth_service':
                return RegisterValidationMiddleware()
  
        return None