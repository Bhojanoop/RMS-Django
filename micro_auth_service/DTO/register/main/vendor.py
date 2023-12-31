from pydantic import BaseModel,validator,constr
import re


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class VendorDTO(BaseModel):
    full_name:constr(min_length=1,max_length=90,strip_whitespace=True)
    email:constr(min_length=1,max_length=90,strip_whitespace=True)
    phone:constr(min_length=10,max_length=10,strip_whitespace=True)
    confirm_password:constr(strip_whitespace=True,max_length=10)=None
    password:constr(min_length=1,strip_whitespace=True,max_length=10)
    referral_code:constr(strip_whitespace=True)=''
    is_notified:bool=False

    @validator('password',allow_reuse=True,always=True)
    def check_password(cls,value,values):
        try:
            if value and values['confirm_password']:
                confirm_password=values['confirm_password']
                if value==confirm_password:
                    return value
                else:
                    raise ValueError("Passwords are not same")
            else:
                return value
        except Exception as e:
            raise Exception(str(e))
    
    
    @validator('email',allow_reuse=True,always=True)
    def check_mail(cls,value):
        try:
            if value:
                if re.fullmatch(email_regex,value):
                    return value
                else:
                    raise ValueError("invalid email!")
        except Exception as e:
            raise Exception(str(e))
    
