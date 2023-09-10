from django.db import models
from datetime import datetime

from micro_brand_service.models.brand import Brand

class Branch(models.Model):
    branch_id=models.CharField(max_length=100,primary_key=True,default="")
    branch_name=models.CharField(max_length=100,null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand_branch')
    created_at=models.CharField(max_length=50,default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.branch_name

class BranchMeta(models.Model):
    branch_meta_id=models.CharField(max_length=100,primary_key=True,default="")
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='branch_meta')
    postal_code=models.CharField(max_length=6,null=True,blank=True)
    city=models.CharField(max_length=30,null=True,blank=True)
    state=models.CharField(max_length=30,null=True,blank=True)
    district=models.CharField(max_length=30,null=True,blank=True)
    address_1=models.CharField(max_length=30,null=True,blank=True)
    address_2=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self) -> str:
        return self.city