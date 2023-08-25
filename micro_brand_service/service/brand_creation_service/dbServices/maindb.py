from micro_brand_service.service.brand_creation_service.dbServices.brand import CreateBrand
from micro_brand_service.service.brand_creation_service.dbServices.brandRole import CreateBrandRoleDefault
from micro_brand_service.service.brand_creation_service.dbServices.brandVerify import CreateBrandVerify

from micro_brand_service.service.brand_creation_service.storeFile.store import StoreFile

class DbService:

    def __init__(self) -> None:
        self._store=StoreFile()

    def _create_brand(self,request:object)->dict:
        try:
            self._store.storeLogo(request)
            return CreateBrand().save(request=request)
        except Exception as e:
            raise Exception(str(e))
    
    def _create_brand_deafult_role(self,request:object)->dict:
        try:
            return CreateBrandRoleDefault().save(request=request)
        except Exception as e:
            raise Exception(str(e)) 
    
    def _create_brand_verify(self,request:object)->dict:
        try:
            self._store.storeGovtFile(request)
            return CreateBrandVerify().save(request=request)
        except Exception as e:
            raise Exception(str(e))
    
    def process(self,request:object):
        try:
            data1=self._create_brand(request)
            data2=self._create_brand_deafult_role(request)
            data3=self._create_brand_verify(request)
            return [data1,data2,data3]
        except Exception as e:
            raise Exception(str(e))
            