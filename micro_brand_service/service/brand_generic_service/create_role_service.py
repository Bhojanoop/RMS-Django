from micro_brand_service.models.brandRoles import BrandRoles
from micro_brand_service.DTO.brand_generic_dto.createRole_dto import BrandCreateRoleDTO

class CreateRoleService:

    def create(self,dto:BrandCreateRoleDTO):
        try:
            BrandRoles.objects.create(
                id=dto.id,
                user=dto.user,
                brand=dto.brand,
                role=dto.role,
                created_at=dto.created_at
            )
        except Exception as e:
            raise Exception(str(e))