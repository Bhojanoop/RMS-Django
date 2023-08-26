from micro_auth_service.DTO.otp.sent_otp_dto import SentOtpDto

from micro_auth_service.service.otp.sent.sent_db import OtpSaveDB
from micro_auth_service.service.otp.sent.sent_phone import OTPPhoneSent



class Sent:

    def __init__(self) -> None:
        self._phone=OTPPhoneSent
        self._db=OtpSaveDB
    
    def sent(self,dto:SentOtpDto)->dict:
        try:
            dbsave=self._db().save(dto=dto)
            if dbsave:
                return self._phone().sent(dto)
        except Exception as e:
            raise Exception(str(e))