from micro_auth_service.DTO.otp.sent_otp_dto import SentOtpDto

from micro_auth_service.service.otp.sent.sent_db import OtpSaveDB
from micro_auth_service.service.otp.sent.sent_email import OTPEmailSent
from micro_auth_service.service.otp.sent.sent_phone import OTPPhoneSent



class Sent:

    def __init__(self) -> None:
        self._email=OTPEmailSent
        self._phone=OTPPhoneSent
        self._db=OtpSaveDB
    
    def sent(self,dto:SentOtpDto)->dict:
        try:
            dbsave=self._db().save(dto=dto)
            if dbsave:
                self._email().sent(dto)
                self._phone().sent(dto)
                return {"info":f"otp sent to {dto.otp_main.email} and {dto.phone}"}
        except Exception as e:
            raise Exception(str(e))