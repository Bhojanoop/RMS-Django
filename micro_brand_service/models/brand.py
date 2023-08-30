from django.db import models
from datetime import datetime
from micro_auth_service.model.admin_model import Admin

class Brand(models.Model):
    brand_id=models.CharField(max_length=100,primary_key=True,default="")
    brand_name=models.CharField(max_length=100,blank=True,null=True)
    brand_logo_filename=models.CharField(max_length=100,blank=True,null=True)
    is_verified=models.BooleanField(default=False)
    verified_by=models.ForeignKey(Admin,on_delete=models.DO_NOTHING,null=True)
    created_at=models.CharField(max_length=50,default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.brand_name