from django.db import models
from datetime import datetime

from micro_auth_service.model.vendor_models import Vendor
from micro_brand_service.models.brand import Brand
from micro_brand_service.models.roles import RolesForBrand

class BrandRoles(models.Model):
    id=models.CharField(max_length=100,primary_key=True,default="")
    user=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='brandroles_user')
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brandroles_brand')
    role=models.ForeignKey(RolesForBrand,on_delete=models.CASCADE,related_name='brandroles_role')
    created_at=models.CharField(max_length=50,default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.brand.brand_name + " " + self.role.role_name