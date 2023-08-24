from dataclasses import dataclass,field
from micro_brand_service.DTO.brand_creation_dto.main import BrandCreateDTO
from datetime import datetime
from micro_auth_service.model.vendor_models import Vendor
from micro_brand_service.models.brand import Brand
from micro_brand_service.models.roles import RolesBrand
import uuid

@dataclass
class BrandCreateDefaultRoleDbDTO:
    request:object=field(default_factory=object)
    id:str=field(default_factory=str)
    user:object=field(default_factory=object)
    brand:object=field(default_factory=object)
    role:object=field(default_factory=object)
    created_at:float=field(default_factory=float)
    main_dto:BrandCreateDTO=field(default_factory=object)

    def __post_init__(self):
        try:
           self.main_dto=BrandCreateDTO(**self.request.data)
           self.id=str(uuid.uuid3(uuid.NAMESPACE_DNS,name=self.main_dto.userId+self.main_dto.brand_name)).strip()
           self.user=Vendor.objects.get(id=self.main_dto.userId)
           self.brand=Brand.objects.get(brand_id=str(uuid.uuid3(uuid.NAMESPACE_DNS,name=self.main_dto.brand_name)).strip())
           self.role=RolesBrand.objects.get(id='1B')
           self.created_at=datetime.now().timestamp()
        except Exception as e:
            raise Exception(str(e))