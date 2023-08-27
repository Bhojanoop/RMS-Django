from micro_auth_service.DTO.otp.otp_dto import OtpDTO
from micro_auth_service.model.vendor_models import Vendor
import json

class OTPValidationMiddleware:

    def __init__(self) -> None:
        self._verificationtypes=['LOGIN','REGISTER']
    
    def _is_verificationType_ok(self,dto:OtpDTO)->bool:
        if dto.verification_type in self._verificationtypes:
            return True
        else:
            return False
    
    def _is_cred_ok(self,dto:OtpDTO)->bool:
        try:
            if dto.verification_type=='LOGIN':
                if Vendor.objects.filter(phone=dto.phone).exists():
                    return True
                else:
                    raise Exception("phone does not exists")
                
            elif dto.verification_type=='REGISTER': 
                if not (Vendor.objects.filter(phone=dto.phone).exists() and Vendor.objects.filter(email=dto.email).exists()):
                    return True
                else:
                    raise Exception("phone or email exists")
        except Exception as e:
            raise Exception(str(e))
    
    def validates(self,request:object):
        try:
            body_unicode = request.body.decode('utf-8')
            _data:dict = json.loads(body_unicode)

            if not _data.get('verify'):
                dto=OtpDTO(**_data)
                self._is_verificationType_ok(dto=dto)
                self._is_cred_ok(dto=dto)
        except Exception as e:
            raise Exception(str(e))

    