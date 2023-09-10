from pydantic import BaseModel,constr

class BranchMainDTO(BaseModel):
    branch_name:constr(min_length=1,strip_whitespace=True)
    brand_id:constr(min_length=1,strip_whitespace=True)
    postal_code:constr(min_length=1,max_length=6,strip_whitespace=True)
    city:constr(min_length=1,strip_whitespace=True)
    state:constr(min_length=1,strip_whitespace=True)
    district:constr(min_length=1,strip_whitespace=True)
    address_1:constr(min_length=1,strip_whitespace=True)
    address_2:constr(strip_whitespace=True)=''
