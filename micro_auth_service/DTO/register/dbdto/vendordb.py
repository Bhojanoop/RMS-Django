from dataclasses import dataclass,field
from django.contrib.auth.hashers import make_password
from micro_auth_service.DTO.register.main.vendor import VendorDTO
import uuid


@dataclass
class VendorDbDTO:
    id:str=field(default_factory=str)
    password:str=field(default_factory=str)
    vendor:VendorDTO=field(default_factory=object)
    request:object=field(default_factory=object)
    
    def __post_init__(self):    
        try:
            self.vendor=VendorDTO(**self.request.data)
            self.password=make_password(self.vendor.password)
            self.id=str(uuid.uuid3(uuid.NAMESPACE_DNS,self.vendor.phone)).strip()
        except Exception as e:
            raise Exception(str(e))
