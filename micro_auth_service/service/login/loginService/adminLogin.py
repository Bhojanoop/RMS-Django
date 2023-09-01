from micro_auth_service.model.admin_model import Admin
from micro_auth_service.DTO.login.login_dto import LoginDTO
from micro_auth_service.jwt.main import JwtBuilder
from django.contrib.auth.hashers import check_password
from micro_auth_service.DTO.login.login_dto import LoginDTO
from datetime import datetime

class AdminLogin:

    def _getAdmin(self,id:str):
        try:
            if not Admin.objects.filter(id=id).exists():
                raise Exception('user not found!')
            admin=Admin.objects.get(id=id)
            return admin
        except Exception as e:
            raise Exception(str(e))
    
    def _password_matched(self,password:str,admin:object):
        _password=admin.password
        return check_password(password,_password)

    def get_tokens(self,dto:LoginDTO,request:object)->dict:
        try:
            admin=self._getAdmin(id=dto.id)

            if self._password_matched(password=dto.password,admin=admin):

                tokens=JwtBuilder(payload={
                    "sub":admin.id,
                    "name":admin.full_name,
                    "type":"admin",
                    "admin_role_id":admin.permission_level
                },request=request).get_token()
                admin.refresh_token=tokens['refresh_token']
                admin.save()
                return {"message":"admin successfully logged in!","token":tokens,"timestamp":datetime.now().timestamp()}
        
            raise Exception("password is not matched")
        except Exception as e:
            raise Exception(str(e))