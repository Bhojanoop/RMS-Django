from micro_brand_service.models.brandVerification import BrandVerification
from micro_brand_service.DTO.brand_main_dto.dbdto.brandVerify_db import BrandCreateVerifyDbDTO

class CreateBrandVerify:

    def save(self,request:object)->dict:
        try:
            dto=BrandCreateVerifyDbDTO(request=request)
            BrandVerification.objects.create(
                brand_verify_id=dto.brand_verify_id,
                user=dto.user,
                brand=dto.brand,
                govt_doc_filename=dto.govt_doc_filename,
                created_at=dto.created_at
            )
            return {
                "brand_verify_id":dto.brand_verify_id,
                "user":dto.user.full_name,
                "brand":dto.brand.brand_name,
                "govt_doc_filename":dto.govt_doc_filename,
                "created_at":dto.created_at
            }
            
        except Exception as e:
            raise Exception(str(e))



