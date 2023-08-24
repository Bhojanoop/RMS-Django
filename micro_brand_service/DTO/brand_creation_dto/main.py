from pydantic import BaseModel,validator,constr

class BrandCreateDTO(BaseModel):
    userId:constr(min_length=1,strip_whitespace=True)
    brand_name:constr(min_length=1,strip_whitespace=True)
    brand_logo_filename:constr(min_length=1,strip_whitespace=True)
    brand_logo_b64encode:constr(min_length=1,strip_whitespace=True)
    govt_doc_filename:constr(min_length=1,strip_whitespace=True)
    govt_doc_b64encode:constr(min_length=1,strip_whitespace=True)

    @validator('brand_logo_b64encode',allow_reuse=True,always=True)
    def arrange_musicFileObj(cls,value):
        try:
            if value:
                return value.split(',')[1]
        except Exception as e:
            raise Exception(str(e))
    
    @validator('govt_doc_b64encode',allow_reuse=True,always=True)
    def arrange_govFileObj(cls,value):
        try:
            if value:
                return value.split(',')[1]
        except Exception as e:
            raise Exception(str(e))