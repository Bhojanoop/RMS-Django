from micro_auth_service.DTO.register.main.admin import AdminDTO
from micro_auth_service.DTO.register.main.vendor import VendorDTO
from micro_auth_service.DTO.register.main.customer import CustomerDTO
from pydantic import ValidationError
import json

class RegisterValidationMiddleware:

    def __init__(self) -> None:
        self._registers={
            "ADMIN":AdminDTO,
            "VENDOR":VendorDTO,
            "CUSTOMER":CustomerDTO
        }

    def validates(self,request:object):
        try:
            body_unicode = request.body.decode('utf-8')
            _data:dict = json.loads(body_unicode)

            arr=request.path.split("/")
            usertype=arr[len(arr)-1].split('=')[1]

            self._registers[usertype.upper()](**_data)

        except ValidationError as e:
            raise Exception(e.errors()[0]['msg'])