from django.db import models
from datetime import datetime

from micro_auth_service.model.vendor_models import Vendor

class Brand(models.Model):
    brand_id=models.CharField(max_length=100,primary_key=True,default="")
    brand_name=models.CharField(max_length=100,blank=True,null=True)
    brand_logo=models.CharField(max_length=100,blank=True,null=True)
    is_verified=models.BooleanField(default=False)
    created_at=models.CharField(max_length=50,default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.brand_name

class BrandVerification(models.Model):
    brand_verify_id=models.CharField(max_length=100,primary_key=True,default="")
    user=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='user_brand_verify',default=None)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand_verification',default=None)
    govt_doc=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.brand.brand_name

class BrandRoles(models.Model):
    brand_roles_id=models.CharField(max_length=100,primary_key=True,default="")
    user=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='user_brand_role',default=None)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand_role',default=None)
    role=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.CharField(max_length=50,default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.brand.brand_name + " " + self.role