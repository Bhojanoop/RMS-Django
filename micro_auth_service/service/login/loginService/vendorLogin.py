from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.DTO.login.login_dto import LoginDTO
from micro_auth_service.jwt.main import JwtBuilder
from django.contrib.auth.hashers import check_password
from micro_auth_service.DTO.login.login_dto import LoginDTO
from datetime import datetime

from micro_brand_service.models.brandRoles import BrandRoles

class VendorLogin:

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

    def _getVendor(self,id:str):
        try:
            if not Vendor.objects.filter(id=id).exists():
                raise Exception('user not found!')
            vendor=Vendor.objects.get(id=id)
            return vendor,self._getRoles(vendor=vendor)
        except Exception as e:
            raise Exception(str(e))
    
    def _password_matched(self,password:str,vendor:object):
        _password=vendor.password
        return check_password(password,_password)

    def get_tokens(self,dto:LoginDTO,request:object)->dict:
        try:
            vendor,roles=self._getVendor(id=dto.id)

            if self._password_matched(password=dto.password,vendor=vendor):

                tokens=JwtBuilder(payload={
                    "sub":vendor.id,
                    "name":vendor.full_name,
                    "type":"vendor",
                    "brand_details":roles[0],
                    "branch_details":roles[1]
                },request=request).get_token()
                
                vendor.refresh_token=tokens['refresh_token']
                vendor.save()
                
                return {"message":"vendor successfully logged in!","token":tokens,"timestamp":datetime.now().timestamp()}

            raise Exception("password is not matched")
        except Exception as e:
            raise Exception(str(e))