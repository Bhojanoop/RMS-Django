from dataclasses import dataclass,field
from micro_brand_service.DTO.brand_creation_dto.main import BrandCreateDTO
from datetime import datetime
from micro_auth_service.model.vendor_models import Vendor
from micro_brand_service.models.brand import Brand
import uuid

@dataclass
class BrandCreateVerifyDbDTO:
    request:object=field(default_factory=object)
    brand_verify_id:str=field(default_factory=str)
    user:object=field(default_factory=object)
    brand:object=field(default_factory=object)
    govt_doc_filename:str=field(default_factory=str)
    created_at:float=field(default_factory=float)
    main_dto:BrandCreateDTO=field(default_factory=object)

    def __post_init__(self):
        try:
           self.main_dto=BrandCreateDTO(**self.request.data)
           self.brand_verify_id=str(uuid.uuid3(uuid.NAMESPACE_DNS,name=self.main_dto.govt_doc_filename)).strip()
           self.user=Vendor.objects.get(id=self.main_dto.userId)
           self.brand=Brand.objects.get(brand_id=str(uuid.uuid3(uuid.NAMESPACE_DNS,name=self.main_dto.brand_name)).strip())
           self.govt_doc_filename=self.main_dto.govt_doc_filename
           self.created_at=datetime.now().timestamp()
        except Exception as e:
            raise Exception(str(e))