from django.db import models

class MailVerify(models.Model):
    email=models.CharField(max_length=50,primary_key=True,default="")
    open_for_verify=models.BooleanField(default=False)
    open_at=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return self.email