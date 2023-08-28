from django.db import models

class Customer(models.Model):
    id=models.CharField(max_length=50,primary_key=True,default="")
    full_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True,unique=True)
    phone=models.CharField(max_length=12,null=True,blank=True,unique=True)

    class Meta:
        indexes=[
            models.Index(fields=['phone','email'])
        ]

    def __str__(self) -> str:
        return self.full_name