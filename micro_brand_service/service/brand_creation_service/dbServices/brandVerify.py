from micro_brand_service.serializer.brandVerify import BrandVerifySerializer
from micro_brand_service.DTO.brand_creation_dto.dbdto.brandVerify_db import BrandCreateVerifyDbDTO

class CreateBrandVerify:

    def save(self,request:object)->dict:
        try:
            dto=BrandCreateVerifyDbDTO(request=request).__dict__
            del dto['request']
            del dto['main_dto']

            serializer=BrandVerifySerializer(data=dto)

            if serializer.is_valid():
                serializer.save()

                return serializer.data
            
            raise Exception(str(serializer.errors))
        except Exception as e:
            raise Exception(str(e))



