from core.utils.filesStore.store import Store

from micro_brand_service.DTO.brand_main_dto.main import BrandCreateDTO

class StoreFile:

    def storeLogo(self,request):
        try:
            dto=BrandCreateDTO(**request.data)
            return Store.store(
                filename=f'brand_logo/'+f'{dto.brand_logo_filename}',
                fileobj=dto.brand_logo_b64encode
            )
        except Exception as e:
            raise Exception(str(e))
    
    def storeGovtFile(self,request):
        try:
            dto=BrandCreateDTO(**request.data)
            return Store.store(
                filename=f'govt/'+f'{dto.govt_doc_filename}',
                fileobj=dto.govt_doc_b64encode
            )
           
        except Exception as e:
            raise Exception(str(e))