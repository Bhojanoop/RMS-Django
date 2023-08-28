from micro_auth_service.model.admin_model import Admin
from micro_auth_service.jwt.main import JwtBuilder
from datetime import datetime

class GetNewTokenAdmin:

    def get_admin(self,userid:str):
        try:
            if not Admin.objects.filter(id=userid).exists():
                raise Exception("user does not exists!")
            return Admin.objects.get(id=userid)
        except Exception as e:
            raise Exception(str(e))

    def get_tokens(self,userid:str,request:object)->dict:
        try:
            admin=self.get_admin(userid=userid)
            tokens=JwtBuilder(payload={
                "sub":admin.id,
                "name":admin.full_name,
                "type":"admin"
            },request=request).get_token()
            admin.refresh_token=tokens['refresh_token']
            admin.save()
            return {"message":"new tokens are created for admin!","token":tokens,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))