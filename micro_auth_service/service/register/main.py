from micro_auth_service.service.register.dbservice.admindb import RegisterAdmin
from micro_auth_service.service.register.dbservice.vendordb import RegisterVendor
from micro_auth_service.service.register.dbservice.customerdb import RegisterCustomer


class MainRegisterService:

    def __init__(self) -> None:
        self._registrations={
            "VENDOR":RegisterVendor,
            "ADMIN":RegisterAdmin,
            "CUSTOMER":RegisterCustomer
        }

    def register(self,request:object,usertype:str):
        try:
            return self._registrations[usertype.upper()]().save(request)
        except Exception as e:
            raise Exception(str(e))