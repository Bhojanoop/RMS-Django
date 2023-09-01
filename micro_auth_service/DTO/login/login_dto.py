from pydantic import BaseModel,constr,validator
import uuid

class LoginDTO(BaseModel):
    phone:constr(min_length=1,strip_whitespace=True)
    password:constr(min_length=1,strip_whitespace=True)
    id:constr(strip_whitespace=True)=''

    @validator('id',allow_reuse=True,always=True)
    def get_id(cls,value,values):
        if values['phone']:
            value=str(uuid.uuid3(uuid.NAMESPACE_DNS,values['phone'])).strip()
            return value

