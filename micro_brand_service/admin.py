from django.contrib import admin
from micro_brand_service.models.brand import Brand
from micro_brand_service.models.brandVerification import BrandVerification
from micro_brand_service.models.brandRoles import BrandRoles

admin.site.register(Brand)
admin.site.register(BrandRoles)
admin.site.register(BrandVerification)