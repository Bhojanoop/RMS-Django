from micro_auth_service.model.admin_model import Admin
from micro_auth_service.DTO.login.login_dto import LoginDTO
from micro_auth_service.jwt.main import JwtBuilder

from datetime import datetime

class AdminLogin:

    def _fetchDetails(self,request:object):
        try:
            dto=LoginDTO(**request.data)
            admin=Admin.objects.get(id=dto.username)
            return admin
        except Exception as e:
            raise Exception(str(e))

    def get_tokens(self,request:str)->dict:
        try:
            admin=self._fetchDetails(request=request)
            tokens=JwtBuilder(payload={
                "username":admin.id,
                "type":"admin",
                "admin_role_id":admin.permission_level
            }).get_token()
            admin.refresh_token=tokens['refresh_token']
            admin.save()
            return {"info":"admin successfully logged in!","token":tokens,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))