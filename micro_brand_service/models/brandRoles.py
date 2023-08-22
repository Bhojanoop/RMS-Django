from django.db import models
from datetime import datetime

from micro_auth_service.model.vendor_models import Vendor
from micro_brand_service.models.brand import Brand

class BrandRoles(models.Model):
    brand_roles_id=models.CharField(max_length=100,primary_key=True,default="")
    user=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='user_brand_role')
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand_role')
    role=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.CharField(max_length=50,default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.brand.brand_name + " " + self.role