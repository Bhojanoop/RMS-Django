from pydantic import BaseModel,constr,validator

class BrandPatchDTO(BaseModel):
    userId:constr(min_length=1,strip_whitespace=True)
    brand_name:constr(strip_whitespace=True)=''
    brand_logo_base64:constr(strip_whitespace=True)=''
    brand_logo_filename:constr(strip_whitespace=True)=''

    @validator('brand_logo_filename',allow_reuse=True,always=True)
    def val(cls,value,values):
        if value: 
            if not values['brand_logo_base64']:
                raise Exception("file base64 must be provided")
            return values['userId']+value
        return value
