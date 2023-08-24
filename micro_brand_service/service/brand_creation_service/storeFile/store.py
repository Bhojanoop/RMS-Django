from core.utils.b64decode.decode import Decode

from micro_brand_service.DTO.brand_creation_dto.main import BrandCreateDTO

class StoreFile:

    def storeLogo(self,request):
        try:
            dto=BrandCreateDTO(**request.data)
            with open(f'media/govt/'+f'{dto.govt_doc_filename}','wb') as f:
                f.write(Decode.decode(dto.govt_doc_b64encode))
                f.close()
            return True
        except Exception as e:
            raise Exception(str(e))
    
    def storeGovtFile(self,request):
        try:
            dto=BrandCreateDTO(**request.data)
            with open(f'media/govt/'+f'{dto.govt_doc_filename}','wb') as f:
                f.write(Decode.decode(dto.govt_doc_b64encode))
                f.close()
            return True
        except Exception as e:
            raise Exception(str(e))