from micro_brand_service.service.brand_creation_service.dbServices.maindb import DbService

class MainService:

    def __init__(self) -> None:
        self._db=DbService()

    def create(self,request:object):
        try:
            return self._db.process(request)
        except Exception as e:
            raise Exception(str(e))