from micro_auth_service.DTO.otp.sent_otp_dto import SentOtpDto

class OTPEmailSent:
    
    def sent(self,dto:SentOtpDto)->bool:
        try:
            print('email')
            return True
        except Exception as e:
            raise Exception(str(e))