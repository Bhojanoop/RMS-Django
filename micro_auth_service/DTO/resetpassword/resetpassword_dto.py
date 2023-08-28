from pydantic import BaseModel,validator,constr,ValidationError

class ResetPasswordDTO(BaseModel):
    phone:constr(min_length=10,max_length=10,strip_whitespace=True)
    confirm_password:constr(min_length=1,strip_whitespace=True,max_length=10)=None
    password:constr(min_length=1,strip_whitespace=True)

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