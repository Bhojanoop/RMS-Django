from django.contrib import admin
from micro_brand_service.models.brand import Brand
from micro_brand_service.models.brandVerification import BrandVerification
from micro_brand_service.models.brandRoles import BrandRoles
from micro_brand_service.models.roles import RolesBrand


admin.site.register(Brand)
admin.site.register(BrandRoles)
admin.site.register(BrandVerification)
admin.site.register(RolesBrand)