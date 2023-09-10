from micro_brand_service.service.brand_main_service.dbServices.brand import CreateBrand
from micro_brand_service.service.brand_main_service.dbServices.brandVerify import CreateBrandVerify
from django.db import transaction
from micro_brand_service.service.brand_main_service.storeFile.store import StoreFile

class DbService:

    def __init__(self) -> None:
        self._store=StoreFile()


    def _create_brand(self,request:object)->dict:
        try:
            self._store.storeLogo(request)
            return CreateBrand().save(request=request)
        except Exception as e:
            raise Exception(str(e))
    
    def _create_brand_verify(self,request:object)->dict:
        try:
            #self._store.storeGovtFile(request)
            return CreateBrandVerify().save(request=request)
        except Exception as e:
            raise Exception(str(e))
    
    def process(self,request:object):
        try:
            with transaction.atomic():
                data1=self._create_brand(request)
                #data3=self._create_brand_verify(request)
                return {
                    "brand":data1
                }
        except Exception as e:
            raise Exception(str(e))
            