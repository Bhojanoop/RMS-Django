from micro_brand_service.DTO.brand_main_dto.dbdto.brandRole_db import BrandCreateDefaultRoleDbDTO
from micro_brand_service.models.brandRoles import BrandRoles

class CreateBrandRoleDefault:

    def save(self,request:object)->dict:
        try:
            dto=BrandCreateDefaultRoleDbDTO(request=request)

            BrandRoles.objects.create(
                id=dto.id,
                user=dto.user,
                brand=dto.brand,
                role=dto.role,
                created_at=dto.created_at
            )
            
            return {
                "id":dto.id,"user":dto.user.full_name,"brand":dto.brand.brand_name,"role":dto.role.role_name,"created_at":dto.created_at
            }

        except Exception as e:
            raise Exception(str(e))



