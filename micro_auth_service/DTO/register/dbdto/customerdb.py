from dataclasses import dataclass,field
from micro_auth_service.DTO.register.main.customer import CustomerDTO
import uuid

@dataclass
class CustomerDbDTO:
    customer:CustomerDTO=field(default_factory=object)
    id:str=field(default_factory=str)
    request:object=field(default_factory=object)

    def __post_init__(self):
        try:
            self.customer=CustomerDTO(**self.request.data)
            self.id=str(uuid.uuid3(uuid.NAMESPACE_DNS,self.customer.phone)).strip()
        except Exception as e:
            raise Exception(str(e))

    