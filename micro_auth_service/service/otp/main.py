from micro_auth_service.service.otp.sent.sent_main import Sent
from micro_auth_service.service.otp.verify.verification import Verify
from micro_auth_service.DTO.otp.sent_otp_dto import SentOtpDto
from micro_auth_service.DTO.otp.otp_dto import OtpDTO

class MainOtpService:

    def process(self,request:object):
        try:
            main_dto=OtpDTO(**request.data)
            if not main_dto.verify:
                return Sent().sent(SentOtpDto(otp_main=main_dto))
            else:
                return Verify().verify(dto=main_dto)
        except Exception as e:
            raise Exception(str(e))