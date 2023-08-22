from dataclasses import dataclass,field
import uuid
from django.contrib.auth.hashers import make_password
from micro_auth_service.DTO.register.main.admin import AdminDTO

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

@dataclass
class AdminDbDTO:
    id:str=field(default_factory=str)
    admin:AdminDTO=field(default_factory=object)
    password:str=field(default_factory=str)
    request:object=field(default_factory=object)
    refresh_token:str=field(default_factory=str)
    
    def __post_init__(self):    
        try:
            self.admin=AdminDTO(**self.request.data)
            self.password=make_password(self.admin.password)
            self.id=str(uuid.uuid3(uuid.NAMESPACE_DNS,self.admin.phone)).strip()
            self.refresh_token=''
        except Exception as e:
            raise Exception(str(e))
