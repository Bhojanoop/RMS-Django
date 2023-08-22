from pydantic import BaseModel,constr

class LoginDTO(BaseModel):
    username:constr(min_length=1,strip_whitespace=True)
    password:constr(min_length=1,strip_whitespace=True)