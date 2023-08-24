from micro_brand_service.serializer.brandCreate import BrandCreateSerializer
from micro_brand_service.DTO.brand_creation_dto.dbdto.brand_db import BrandCreateDbDTO

class CreateBrand:

    def save(self,request:object)->dict:
        try:
            dto=BrandCreateDbDTO(request=request).__dict__
            main_dto=dto['main_dto'].__dict__
            del dto['request']
            del dto['main_dto']
            del main_dto['userId']
            del main_dto['brand_logo_b64encode']
            del main_dto['govt_doc_filename']
            del main_dto['govt_doc_b64encode']

            data=dto|main_dto

            serializer=BrandCreateSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

                return serializer.data
            
            raise Exception(str(serializer.errors))
        except Exception as e:
            raise Exception(str(e))



