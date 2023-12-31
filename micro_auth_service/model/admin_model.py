from django.db import models
from django.contrib.auth.hashers import check_password

PERMISSION_LEVEL=(
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)

class Admin(models.Model):
    id=models.CharField(max_length=50,primary_key=True,default="")
    full_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=12,null=True,blank=True,unique=True)
    password=models.CharField(max_length=350,null=True,blank=True,unique=True)
    permission_level=models.CharField(max_length=1,null=True,blank=True,choices=PERMISSION_LEVEL,default='1')
    refresh_token=models.TextField(default="",null=True,blank=True)

    class Meta:
        indexes=[
            models.Index(fields=['phone','email'])
        ]

    def is_valid_password(self,password):
        return check_password(password,self.password)

    def __str__(self) -> str:
        return self.full_name