from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.jwt.main import JwtBuilder
from datetime import datetime

class GetNewTokenVendor:

    def get_vendor(self,userid:str):
        try:
            if not Vendor.objects.filter(id=userid).exists():
                raise Exception("user does not exists!")
            return Vendor.objects.get(id=userid)
        except Exception as e:
            raise Exception(str(e))

    def get_tokens(self,userid:str)->dict:
        try:
            vendor=self.get_vendor(userid=userid)
            tokens=JwtBuilder(payload={
                "sub":vendor.id,
                "name":vendor.full_name,
                "type":"vendor"
            }).get_token()
            vendor.refresh_token=tokens['refresh_token']
            vendor.save()
            return {"info":"new tokens are created for vendor!","token":tokens,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))