from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.DTO.login.login_dto import LoginDTO
from micro_auth_service.jwt.main import JwtBuilder

from micro_brand_service.models.brandRoles import BrandRoles

from datetime import datetime

class VendorLogin:

    def _getVendor(self,request:object):
        try:
            dto=LoginDTO(**request.data)
            vendor=Vendor.objects.filter(phone=dto.username)
            #brand_role_name=''
            #brand_role_id=''
            #brand_name=''
            #if BrandRoles.objects.select_related('user') and BrandRoles.objects.select_related('user').get(user=vendor):
            #    brand=BrandRoles.objects.select_related('user').get(user=vendor)
            #    brand_role_name=brand.role
            #    brand_role_id=brand.brand_roles_id
            #    brand_name=brand.brand.brand_name
            return vendor
        except Exception as e:
            raise Exception(str(e))

    def get_tokens(self,request:str)->dict:
        try:
            vendor=self._getVendor(request=request)
            tokens=JwtBuilder(payload={
                "sub":vendor.values('id')[0]['id'],
                "name":vendor.values('full_name')[0]['full_name'],
                "type":"vendor"
            }).get_token()
            vendor.update(refresh_token=tokens['refresh_token'])
            return {"message":"vendor successfully logged in!","token":tokens,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))