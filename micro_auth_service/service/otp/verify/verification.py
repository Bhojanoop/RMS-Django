from micro_auth_service.DTO.otp.otp_dto import OtpDTO
from micro_auth_service.model.otp_model import OTP
from datetime import datetime
from django.db import transaction

class Verify:

    def verify(self,dto:OtpDTO)->dict:
        try:
            with transaction.atomic():
                if OTP.objects.filter(verifiable_cred=dto.phone).exists():
                    obj=OTP.objects.get(verifiable_cred=dto.phone)
                    if(int(obj.otp)==int(dto.otp) and float(obj.expiry))>datetime.timestamp(datetime.now()):
                        obj.delete()
                        return {"message":f"Verification done for {dto.phone}!","timestamp":datetime.now().timestamp()}
                    elif (int(obj.otp)!=int(dto.otp) and float(obj.expiry))>datetime.timestamp(datetime.now()):
                        raise Exception("Wrong OTP. If you miss otp you can resend it!")
                    else:
                        obj.delete()
                        raise Exception("Invalid OTP!")
                else:
                    raise Exception("credential for otp verify does not match!")
        except Exception as e:
            raise Exception(str(e))