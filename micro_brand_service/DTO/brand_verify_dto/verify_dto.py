from pydantic import BaseModel,constr,validator

class BrandVerifyDTO(BaseModel):
    verified_by:constr(min_length=1,strip_whitespace=True)
    verification_id:constr(min_length=1,strip_whitespace=True)
