from django.db import models

class OTP(models.Model):
    verifiable_cred=models.CharField(max_length=50,primary_key=True,default="")
    otp=models.IntegerField(default=0)
    expiry=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self) -> str:
        return self.verifiable_cred