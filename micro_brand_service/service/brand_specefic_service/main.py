from micro_brand_service.models.brand import Brand
from datetime import datetime
from micro_brand_service.serializer.brandGet import BrandGetSerializer
from micro_brand_service.DTO.brand_specefic_dto.patch_dto import BrandPatchDTO
from micro_brand_service.service.brand_specefic_service.patch.patchs import Patch

class BrandSpeceficService:

    def patch(self,request:object,brand_id:str):
        try:
            dto=BrandPatchDTO(**request.data)
            brand=Brand.objects.get(brand_id=brand_id)
            return Patch().patch_brand(brand=brand,dto=dto)
        except Exception as e:
            raise Exception(str(e))
    
    def delete(self,brand_id:str):
        try:
            brand=Brand.objects.get(brand_id=brand_id)
            brand.delete()
            return {"message":"successfully deleted!","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))
    
    def get(self,brand_id:str):
        try:
            brand=Brand.objects.get(brand_id=brand_id)
            data=BrandGetSerializer(brand,many=False).data
            return {"message":"successfully fetched!","brand":data,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))
