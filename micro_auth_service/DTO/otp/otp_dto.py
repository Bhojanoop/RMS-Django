from pydantic import BaseModel,constr,validator

class OtpDTO(BaseModel):
    phone:constr(min_length=1,strip_whitespace=True)
    otp:constr(strip_whitespace=True,max_length=6)=None # only given when verify=True
    verify:bool=False #False means just sent otp and True means verify otp
