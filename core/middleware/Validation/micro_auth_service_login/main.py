from micro_auth_service.DTO.login.login_dto import LoginDTO
from micro_auth_service.model.admin_model import Admin
from micro_auth_service.model.vendor_models import Vendor
import json

class LoginValidationMiddleware:

    def __init__(self) -> None:
        self._logins={
            "ADMIN":Admin,
            "VENDOR":Vendor
        }

    def has_user(self,username:str,DB:object)->bool:
        return DB.objects.filter(id=username).exists()
    
    def password_matched(self,password:str,username:str,DB:object):
        return DB.objects.get(id=username).is_valid_password(password)

    def validates(self,request:object):
        try:
            body_unicode = request.body.decode('utf-8')
            _data:dict = json.loads(body_unicode)
            dto=LoginDTO(**_data)
            arr=request.path.split("/")
            usertype=arr[len(arr)-1].split('=')[1]
            db=self._logins[usertype.upper()]
            
            if not self.has_user(username=dto.username,DB=db):
                raise Exception("user doesn't exists!")
            
            if not self.password_matched(password=dto.password,DB=db,username=dto.username):
                raise Exception("password doesn't match!")

        except Exception as e:
            raise Exception(str(e))