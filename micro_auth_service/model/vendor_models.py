from django.db import models
from django.contrib.auth.hashers import check_password

class Vendor(models.Model):
    id=models.CharField(max_length=50,primary_key=True,default="")
    full_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True,unique=True)
    phone=models.CharField(max_length=12,null=True,blank=True,unique=True)
    password=models.CharField(max_length=350,null=True,blank=True)
    referral_code=models.CharField(max_length=20,null=True,blank=True)
    is_notified=models.BooleanField(default=False)
    refresh_token=models.TextField(default="",null=True,blank=True)

    def is_valid_password(self,password):
        return check_password(password,self.password)

    def __str__(self) -> str:
        return self.full_name