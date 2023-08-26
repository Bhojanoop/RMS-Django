from dataclasses import dataclass,field
from micro_auth_service.DTO.otp.otp_dto import OtpDTO
import random
from datetime import datetime,timedelta
from micro_auth_service.model.admin_model import Admin
from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.model.customer_model import Customer

@dataclass
class SentOtpDto:
    otp_main:OtpDTO=field(default_factory=object)
    sentable_otp:int=field(default_factory=int)
    expiry:float=field(default_factory=float)
    phone:str=field(default_factory=str)

    def __post_init__(self):
        try:
            self.sentable_otp=random.randint(000000,999999)
            self.expiry=datetime.timestamp(datetime.now()+timedelta(minutes=3))
            if self.otp_main.user_type.upper()=='ADMIN':
                if Admin.objects.filter(email=self.otp_main.email).exists():
                    self.phone=Admin.objects.filter(email=self.otp_main.email).values('phone')[0]['phone']
                else:
                    raise Exception("email not found")
            elif self.otp_main.user_type.upper()=='VENDOR':
                if Vendor.objects.filter(email=self.otp_main.email).exists():
                    self.phone=Vendor.objects.filter(email=self.otp_main.email).values('phone')[0]['phone']
                else:
                    raise Exception("email not found")
            
            elif self.otp_main.user_type.upper()=='CUSTOMER':
                if Customer.objects.filter(email=self.otp_main.email).exists():
                    self.phone=Customer.objects.filter(email=self.otp_main.email).values('phone')[0]['phone']
                else:
                    raise Exception("email not found")
            
        except Exception as e:
            raise Exception(str(e))