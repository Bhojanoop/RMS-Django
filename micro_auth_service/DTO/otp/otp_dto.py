from pydantic import BaseModel,constr,validator
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class OtpDTO(BaseModel):
    phone:constr(min_length=10,max_length=10,strip_whitespace=True)
    email:constr(strip_whitespace=True)='' # when verification type register
    verification_type:constr(strip_whitespace=True)='' # if login then logic type login else register
    verify:bool=False #False means just sent otp and True means verify otp
    otp:constr(strip_whitespace=True,max_length=6)='' # only given when verify=True
    
    @validator('otp',allow_reuse=True,always=True)
    def otp_and_verify_validate(cls,value,values):
        if value and values['verify']==False:
            raise Exception("for otp make sure verify is True!")
        return value
    
    @validator('verification_type',allow_reuse=True,always=True)
    def verification_type_validate(cls,value):
        if value:
            if not value.upper() in ['NEW_USER','NOT_NEW_USER']:
                raise Exception("verification_type must be either new_user or not_new_user")
            return value.upper()
    
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
