from pydantic import BaseModel,validator,constr
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class CustomerDTO(BaseModel):
    full_name:constr(min_length=1,max_length=90,strip_whitespace=True)
    email:constr(min_length=1,max_length=90,strip_whitespace=True)=None
    phone:constr(min_length=10,max_length=10,strip_whitespace=True)

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
