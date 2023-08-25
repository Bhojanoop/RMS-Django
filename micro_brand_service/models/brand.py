from django.db import models
from datetime import datetime

class Brand(models.Model):
    brand_id=models.CharField(max_length=100,primary_key=True,default="")
    brand_name=models.CharField(max_length=100,blank=True,null=True)
    brand_logo_filename=models.CharField(max_length=100,blank=True,null=True)
    is_verified=models.BooleanField(default=False)
    created_at=models.CharField(max_length=50,default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.brand_name