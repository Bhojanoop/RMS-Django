from pydantic import BaseModel,constr,validator

class BrandPatchDTO(BaseModel):
    brand_name:constr(strip_whitespace=True)=''
    brand_logo_base64:constr(strip_whitespace=True)=''
    brand_logo_filename:constr(strip_whitespace=True)=''

    @validator('brand_logo_filename',allow_reuse=True,always=True)
    def val(cls,value,values):
        if value: 
            if not values['brand_logo_base64']:
                raise Exception("file base64 must be provided")
            return value
        return value
