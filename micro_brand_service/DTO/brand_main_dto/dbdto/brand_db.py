from dataclasses import dataclass,field
from micro_brand_service.DTO.brand_main_dto.main import BrandCreateDTO
from datetime import datetime
import uuid

@dataclass
class BrandCreateDbDTO:
    request:object=field(default_factory=object)
    brand_id:str=field(default_factory=str)
    is_verified:bool=True
    created_at:float=field(default_factory=float)
    main_dto:BrandCreateDTO=field(default_factory=object)

    def __post_init__(self):
        try:
           self.main_dto=BrandCreateDTO(**self.request.data)
           self.brand_id=str(uuid.uuid3(uuid.NAMESPACE_DNS,name=self.main_dto.brand_name)).strip()
           self.created_at=datetime.now().timestamp()
        except Exception as e:
            raise Exception(str(e))