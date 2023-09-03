from micro_brand_service.serializer.brandGetVerifications import BrandVerifySerializer
from micro_brand_service.models.brandVerification import BrandVerification
from datetime import datetime
from micro_brand_service.DTO.brand_verify_dto.verify_dto import BrandVerifyDTO
from micro_brand_service.DTO.brand_generic_dto.createRole_dto import BrandCreateRoleDTO
from micro_auth_service.model.admin_model import Admin
from micro_brand_service.models.roles import RolesForBrand
from micro_brand_service.service.brand_generic_service.create_role_service import CreateRoleService

class BrandVerifyMainService:

    def getAll(self,request):
        try:
            q=BrandVerification.objects.all()
            data=BrandVerifySerializer(q,many=True).data
            return {"message":"all brand verifications!","data":data,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))
    
    def verify(self,request):
        try:
            dto=BrandVerifyDTO(**request.data)
            brand_verify_obj=BrandVerification.objects.get(brand_verify_id=dto.verification_id)
            brand=brand_verify_obj.brand
            brand.is_verified=True
            admin=Admin.objects.get(id=dto.verified_by)
            brand.verified_by=admin
            brand.save()

            #make the user as a default super admin
            CreateRoleService().create(
                BrandCreateRoleDTO(user=brand_verify_obj.user,brand=brand,role=RolesForBrand.objects.get(id='1B'))
            )

            #send mail
            return {"message":"brand is verified","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))
    
    def reject(self,request):
        try:
            dto=BrandVerifyDTO(**request.data)
            brand_verify_obj=BrandVerification.objects.get(brand_verify_id=dto.verification_id)
            brand=brand_verify_obj.brand
            brand_user=brand_verify_obj.user
            
            #send rejection mail

            brand.delete()
            return {"message":"rejected successfully!","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))