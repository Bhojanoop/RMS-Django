from micro_auth_service.DTO.otp.sent_otp_dto import SentOtpDto
from datetime import datetime

class OTPPhoneSent:
    
    def sent(self,dto:SentOtpDto)->bool:
        try:
            print('phone')
            return {"message":f"OTP sent successfully!","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))