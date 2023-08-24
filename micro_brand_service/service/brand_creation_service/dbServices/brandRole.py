from micro_brand_service.serializer.brandRole import BrandCreateRoleSerializer
from micro_brand_service.DTO.brand_creation_dto.dbdto.brandRole_db import BrandCreateDefaultRoleDbDTO

class CreateBrandRoleDefault:

    def save(self,request:object)->dict:
        try:
            dto=BrandCreateDefaultRoleDbDTO(request=request).__dict__
            del dto['request']
            del dto['main_dto']

            serializer=BrandCreateRoleSerializer(data=dto)

            if serializer.is_valid():
                serializer.save()

                return serializer.data
            
            raise Exception(str(serializer.errors))
        except Exception as e:
            raise Exception(str(e))



