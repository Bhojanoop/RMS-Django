from micro_auth_service.model.admin_model import Admin
from micro_auth_service.DTO.login.login_dto import LoginDTO
from micro_auth_service.jwt.main import JwtBuilder

from datetime import datetime

class AdminLogin:

    def _getAdmin(self,request:object):
        try:
            dto=LoginDTO(**request.data)
            admin=Admin.objects.filter(email=dto.username)
            return admin
        except Exception as e:
            raise Exception(str(e))

    def get_tokens(self,request:str)->dict:
        try:
            admin=self._getAdmin(request=request)
            print(admin)
            tokens=JwtBuilder(payload={
                "sub":admin.values('id')[0]['id'],
                "name":admin.values('full_name')[0]['full_name'],
                "type":"admin",
                "admin_role_id":admin.values('permission_level')[0]['permission_level']
            }).get_token()
            admin.update(refresh_token=tokens['refresh_token'])
            return {"info":"admin successfully logged in!","token":tokens,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))