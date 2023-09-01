from pydantic import BaseModel,constr,validator
import re
from micro_auth_service.model.vendor_models import Vendor
from micro_auth_service.model.admin_model import Admin
from micro_auth_service.model.customer_model import Customer

def _is_cred_ok(verification_type,phone,email,db):
    if verification_type=='NOT_NEW_USER':
        if db.objects.filter(phone=phone).exists():
            return True
        else:
            raise Exception("phone does not exists")
                
    elif verification_type=='NEW_USER': 
        if db.objects.filter(phone=phone).exists():
            raise Exception("phone already exists")
        if email:
            if Vendor.objects.filter(email=email).exists():
                raise Exception("email already exists")

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class OtpDTO(BaseModel):
    email:constr(strip_whitespace=True)='' # when verification type register
    verification_type:constr(strip_whitespace=True)='' # if login then logic type login else register
    verify:bool=False #False means just sent otp and True means verify otp
    user_type:constr(strip_whitespace=True)='' #either admin,or vendor or customer
    otp:constr(strip_whitespace=True,max_length=6)='' # only given when verify=True
    phone:constr(min_length=10,max_length=10,strip_whitespace=True)
    
    @validator('otp',allow_reuse=True,always=True)
    def otp_and_verify_validate(cls,value,values):
        if value and values['verify']==False:
            raise Exception("for otp make sure verify is True!")
        return value
    
    @validator('phone',allow_reuse=True,always=True)
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
                    verification_type=values['verification_type'],
                    phone=value,
                    email=values['email'],
                    db=db
                )
            return value
        except Exception as e:
            raise Exception(str(e))

    
    @validator('user_type',allow_reuse=True,always=True)
    def otp_and_verify_validate(cls,value,values):

        if values['verify']==False and value:
            if value.upper() in ['ADMIN','VENDOR','CUSTOMER']:
                return value
            raise Exception("user type not matched")
        return
        
    
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
