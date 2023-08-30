from micro_brand_service.serializer.brandGetVerifications import BrandVerifySerializer
from micro_brand_service.models.brandVerification import BrandVerification
from datetime import datetime
from micro_brand_service.DTO.brand_verify_dto.verify_dto import BrandVerifyDTO
from micro_brand_service.models.brand import Brand
from micro_auth_service.model.admin_model import Admin

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
            brand=Brand.objects.get(brand_id=dto.brand_id)
            brand.is_verified=True
            admin=Admin.objects.get(id=dto.verified_by)
            brand.verified_by=admin
            brand.save()
            return {"message":"brand is verified","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))