from micro_auth_service.serializer.register.customer import CustomerRegisterSerializer
from micro_auth_service.DTO.register.customerdb import CustomerDbDTO
from datetime import datetime

class RegisterCustomer:

    def save(self,request:object)->dict:
        try:
            data=CustomerDbDTO(**request.data).__dict__
            serializer=CustomerRegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return {"data":serializer.data,"info":"customer registration complete!","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))