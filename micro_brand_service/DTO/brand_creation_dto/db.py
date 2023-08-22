from dataclasses import dataclass,field
from micro_brand_service.DTO.brand_creation_dto.main import BrandCreateDTO
from datetime import datetime

@dataclass
class DbBrandCreateDTO:
    request:object=field(default_factory=object)
    role:str=field(default_factory=str)
    created_at:float=field(default_factory=float)
    main_dto:BrandCreateDTO=field(default_factory=object)

    def __post_init__(self):
        try:
           self.main_dto=BrandCreateDTO(**self.request.data)
           self.role="admin"
           self.created_at=datetime.now().timestamp()
        except Exception as e:
            raise Exception(str(e))