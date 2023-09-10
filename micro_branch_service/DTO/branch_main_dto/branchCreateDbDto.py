from dataclasses import dataclass,field
from micro_branch_service.DTO.branch_main_dto.main import BranchMainDTO
from micro_brand_service.models.brand import Brand
from datetime import datetime
import uuid

@dataclass
class BranchCreateDbDTO:
    request:object=field(default_factory=object)
    main_dto:BranchMainDTO=field(default_factory=object)
    branch_id:str=field(default_factory=str)
    branch_meta_id:str=field(default_factory=str)
    created_at:float=field(default_factory=float)
    brand:object=field(default_factory=object)

    def __post_init__(self):
        try:
            self.main_dto=BranchMainDTO(**self.request.data)
            self.branch_id=str(uuid.uuid3(uuid.NAMESPACE_DNS,self.main_dto.branch_name)).strip()
            self.branch_meta_id=str(uuid.uuid3(uuid.NAMESPACE_DNS,self.main_dto.branch_name+self.main_dto.postal_code)).strip()
            self.created_at=datetime.now().timestamp()
            self.brand=Brand.objects.get(brand_id=self.main_dto.brand_id)
        except Exception as e:
            raise Exception(str(e))