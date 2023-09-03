from dataclasses import dataclass,field
from datetime import datetime
import uuid

@dataclass
class BrandCreateRoleDTO:
    id:str=field(default_factory=str)
    user:object=field(default_factory=object)
    brand:object=field(default_factory=object)
    role:object=field(default_factory=object)
    created_at:float=field(default_factory=float)

    def __post_init__(self):
        try:
           self.id=str(uuid.uuid3(uuid.NAMESPACE_DNS,name=self.user.id+self.brand.brand_id)).strip()
           self.created_at=datetime.now().timestamp()
        except Exception as e:
            raise Exception(str(e))