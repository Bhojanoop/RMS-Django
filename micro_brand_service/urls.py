from django.urls import path,re_path
from micro_brand_service.controller.brandmainController import BrandMainController

urlpatterns = [
    re_path(r'(?:/(\d+))?',BrandMainController.as_view())
]
