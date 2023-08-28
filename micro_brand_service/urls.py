from django.urls import path,re_path
from micro_brand_service.controller.brandmainController import BrandMainController
from micro_brand_service.controller.brandspeceficController import BrandSpeceficController

urlpatterns = [
    re_path(r'main/(?:/(\d+))?',BrandMainController.as_view()),
    path('specefic/brand_id=<str:brand_id>',BrandSpeceficController.as_view())
]
