from micro_auth_service.DTO.otp.sent_otp_dto import SentOtpDto
from micro_auth_service.model.otp_model import OTP
from django.db import transaction

class OtpSaveDB:

    def save(self,dto:SentOtpDto)->bool:
        try:
            with transaction.atomic():
                if OTP.objects.filter(verifiable_cred=dto.otp_main.phone).exists():
                    otp_obj=OTP.objects.get(verifiable_cred=dto.otp_main.phone)
                    otp_obj.otp=dto.sentable_otp
                    otp_obj.expiry=dto.expiry
                    otp_obj.save()
                else:
                    OTP.objects.create(
                        verifiable_cred=dto.otp_main.phone,
                        otp=dto.sentable_otp,
                        expiry=dto.expiry
                    )
                return True
        except Exception as e:
            raise Exception(str(e))