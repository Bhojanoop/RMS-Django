from pydantic import BaseModel,constr,validator
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class OtpDTO(BaseModel):
    email:constr(min_length=1,strip_whitespace=True) #email or phone
    otp:constr(strip_whitespace=True,max_length=6)=None # only given when verify=True
    verify:bool=False #False means just sent otp and True means verify otp
    user_type:constr(min_length=1,strip_whitespace=True)

    
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