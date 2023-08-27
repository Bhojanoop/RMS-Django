from micro_auth_service.serializer.register.customer import CustomerRegisterSerializer
from micro_auth_service.DTO.register.dbdto.customerdb import CustomerDbDTO
from datetime import datetime

class RegisterCustomer:

    def save(self,request:object)->dict:
        try:
            dto=CustomerDbDTO(request=request)
            customer_dto=dto.customer.__dict__
            dbdto=dto.__dict__
            del dbdto['customer']
            del dbdto['request']
            data=dbdto|customer_dto
            print(data)
            serializer=CustomerRegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return {"data":serializer.data,"message":"customer is created!","timestamp":datetime.now().timestamp()}
            else:
                raise Exception(str(serializer.errors))
        except Exception as e:
            raise Exception(str(e))