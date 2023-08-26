from micro_brand_service.service.brand_main_service.dbServices.maindb import DbService
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from micro_brand_service.serializer.brandGetAll import BrandGetAllSerializer
from micro_brand_service.models.brand import Brand

class MainService:

    def __init__(self) -> None:
        self._db=DbService()

    def getAll(self,page):
        try:
            q=Brand.objects.all().order_by('brand_id')
            paginator=Paginator(q,10)
            try:
                query=paginator.page(page)
            except PageNotAnInteger:
                query=paginator.page(1)
            except EmptyPage:
                query=paginator.page(paginator.num_pages)
            data=BrandGetAllSerializer(query,many=True).data
            return {"brand":data}
        except Exception as e:
            raise Exception(str(e))

    def create(self,request:object):
        try:
            return self._db.process(request)
        except Exception as e:
            raise Exception(str(e))