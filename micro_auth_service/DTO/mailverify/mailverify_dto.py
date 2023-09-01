from pydantic import BaseModel,validator,constr
import re
from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.model.admin_model import Admin
from micro_auth_service.model.customer_model import Customer

def _is_cred_ok(email,db):
    if db.objects.filter(email=email).values('email_verified_at')[0]['email_verified_at']:
        raise Exception("already verified")
    else:
        return

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class MailVerifyDTO(BaseModel):
    user_type:constr(strip_whitespace=True)='' #either admin,or vendor or customer
    email:constr(max_length=50,min_length=1,strip_whitespace=True)
   
    
    @validator('email',allow_reuse=True,always=True)
    def validate_email(cls,value):
        try:
            if value:
                if re.fullmatch(email_regex,value):
                    return value
                else:
                    raise ValueError("invalid email!")
        except Exception as e:
            raise Exception(str(e))
    
    @validator('user_type',allow_reuse=True,always=True)
    def otp_and_verify_validate(cls,value):
        if value:
            if value.upper() in ['ADMIN','VENDOR','CUSTOMER']:
                return value
            raise Exception("user type not matched")
    
    @validator('email',allow_reuse=True,always=True)
    def val_is_cred_ok(cls,value,values):
        try:
            if values['user_type']:
                if values['user_type'].upper()=='VENDOR':
                    db=Vendor
                elif values['user_type'].upper()=='ADMIN':
                    db=Admin
                elif values['user_type'].upper()=='CUSTOMER':
                    db=Customer
                _is_cred_ok(
                    email=value,
                    db=db
                )
            return value
        except Exception as e:
            raise Exception(str(e))