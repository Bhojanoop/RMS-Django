from django.urls import path
from micro_brand_service.controller.brandmainController import BrandCreateController

urlpatterns = [
    path('create',BrandCreateController.as_view())
]
