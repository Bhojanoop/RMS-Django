from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.DTO.resetpassword.resetpassword_dto import ResetPasswordDTO
from datetime import datetime
from django.contrib.auth.hashers import make_password

class VendorResetPassword:

    def reset(self,dto:ResetPasswordDTO)->dict:
        try:
            Vendor.objects.filter(phone=dto.phone).update(password=make_password(dto.password))
            return {"message":"password is updated!","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))