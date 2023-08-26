from micro_auth_service.model.mailverify_model import MailVerify
from micro_auth_service.model.vendor_models import Vendor
from datetime import datetime

class MainMailVerifyService:

    def is_exists(self,email):
        try:
            if MailVerify.objects.filter(email=email).exists():
                MailVerify.objects.filter(email=email).delete()
                return True
            else:
                raise Exception("not valid")
        except Exception as e:
            raise Exception(str(e))

    def verify(self,email):
        try:
            is_exists=self.is_exists(email)
            if is_exists:
                Vendor.objects.filter(email=email).update(email_verified_at=str(datetime.timestamp(datetime.now())))
                return True
            return False
        except Exception as e:
            raise Exception(str(e))