from micro_auth_service.serializer.register.vendor import VendorRegisterSerializer
from micro_auth_service.DTO.register.vendordb import VendorDbDTO
from datetime import datetime

class RegisterVendor:

    def save(self,request:object)->dict:
        try:
            data=VendorDbDTO(**request.data).__dict__
            print(data)
            del data['confirm_password']
            serializer=VendorRegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                del serializer.data['password']
                return {"data":serializer.data,"info":"vendor registration complete!","timestamp":datetime.now().timestamp()}
        except Exception as e:
            raise Exception(str(e))