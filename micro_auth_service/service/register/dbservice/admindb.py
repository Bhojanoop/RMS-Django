from micro_auth_service.serializer.register.admin import AdminRegisterSerializer
from micro_auth_service.DTO.register.admindb import AdminDbDTO
from datetime import datetime

class RegisterAdmin:

    def save(self,request:object)->dict:
        try:
            data=AdminDbDTO(**request.data).__dict__
            del data['confirm_password']
            serializer=AdminRegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                del serializer.data['password']
                return {"data":serializer.data,"info":"admin registration complete!","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))