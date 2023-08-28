from django.db import models

class RolesForBrand(models.Model):
    id=models.CharField(max_length=50,primary_key=True,default="")
    role_name=models.CharField(max_length=30,unique=True,blank=True,null=True)
    role_desc=models.CharField(max_length=30,unique=True,blank=True,null=True)

    class Meta:
        indexes=[
            models.Index(fields=['role_name'])
        ]

    def __str__(self) -> str:
        return self.role_name
