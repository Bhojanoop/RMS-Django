from pydantic import BaseModel,constr,validator
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class OtpDTO(BaseModel):
    phone:constr(min_length=10,max_length=10,strip_whitespace=True)
    verification_type:constr(min_length=1,strip_whitespace=True) # if login then logic type login else register
    email:constr(min_length=1,strip_whitespace=True)=None # when verification type register
    otp:constr(strip_whitespace=True,max_length=6)=None # only given when verify=True
    verify:bool=False #False means just sent otp and True means verify otp

    @validator('verification_type',allow_reuse=True,always=True)
    def if_email(cls,value,values):
        try:
            if value and value.upper()=='REGISTER':
                if not values['email']:
                    raise Exception("register type must need email!")
                return value.upper()
        except Exception as e:
            raise Exception(str(e))
    
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
