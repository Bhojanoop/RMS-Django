from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.jwt.main import JwtBuilder
from datetime import datetime

from micro_brand_service.models.brandRoles import BrandRoles

class GetNewTokenVendor:

    def _getRoles(self,vendor:object):
        try:
            brand_details=[]
            branch_details=[]

            if BrandRoles.objects.select_related('user').filter(user=vendor):
                brand=BrandRoles.objects.select_related('user').filter(user=vendor)
                for i in brand:
                     obj={
                         "brand_id":i.brand.brand_id,
                         "role_name":i.role.role_name,
                         "role_id":i.role.id,
                     }
                     brand_details.append(obj)
            
            #same for branch

            return brand_details,branch_details
        except Exception as e:
            raise Exception(str(e))

    def get_vendor(self,userid:str):
        try:
            if not Vendor.objects.filter(id=userid).exists():
                raise Exception("user does not exists!")
            
            vendor=Vendor.objects.get(id=userid)
            return vendor,self._getRoles(vendor=vendor)
        except Exception as e:
            raise Exception(str(e))

    def get_tokens(self,userid:str,request:object)->dict:
        try:
            
            vendor,roles=self.get_vendor(userid=userid)
            tokens=JwtBuilder(payload={
                "sub":vendor.id,
                "name":vendor.full_name,
                "type":"vendor",
                "brand_details":roles[0],
                "branch_details":roles[1]
            },request=request).get_token()

            vendor.refresh_token=tokens['refresh_token']
            vendor.save()
            
            return {"message":"new tokens are created for vendor!","token":tokens,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))