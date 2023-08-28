from micro_brand_service.DTO.brand_specefic_dto.patch_dto import BrandPatchDTO
from core.utils.filesStore.store import Store
from micro_brand_service.serializer.brandGet import BrandGetSerializer
from datetime import datetime

class Patch:

    def patch_brand(self,brand:object,dto:BrandPatchDTO):
        try:
            if dto.brand_name:
                brand.brand_name=dto.brand_name
                brand.save()
            if dto.brand_logo_filename:
                Store.store(
                filename=f'brand_logo/'+f'{dto.brand_logo_filename}',
                fileobj=dto.brand_logo_base64
                )
                brand.brand_logo_filename=dto.brand_logo_filename
                brand.save()
            data=BrandGetSerializer(brand,many=False).data
            return {"message":"successfully updated!","brand":data,"timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))