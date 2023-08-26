from micro_auth_service.DTO.otp.otp_dto import OtpDTO
from micro_auth_service.model.otp_model import OTP
from datetime import datetime

class Verify:

    def verify(self,dto:OtpDTO)->dict:
        try:
            if OTP.objects.get(verifiable_cred=dto.phone):
                obj=OTP.objects.get(verifiable_cred=dto.phone)
                if(int(obj.otp)==int(dto.otp) and float(obj.expiry))>datetime.timestamp(datetime.now()):
                    obj.delete()
                    return {"info":f"Verification done for {dto.phone}!"}
                elif (int(obj.otp)!=int(dto.otp) and float(obj.expiry))>datetime.timestamp(datetime.now()):
                    return {"info":"Wrong OTP. If you miss otp you can resend it!"}
                else:
                    obj.delete()
                    return {"info":"Invalid OTP!"}
            else:
                raise Exception("credential for otp does not match!")
        except Exception as e:
            raise Exception(str(e))