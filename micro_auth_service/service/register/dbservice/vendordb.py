from micro_auth_service.serializer.register.vendor import VendorRegisterSerializer
from micro_auth_service.DTO.register.dbdto.vendordb import VendorDbDTO
from datetime import datetime

class RegisterVendor:

    def save(self,request:object)->dict:
        try:
            dto=VendorDbDTO(request=request)
            vendor_dto=dto.vendor.__dict__
            del vendor_dto['password']
            del vendor_dto['confirm_password']
            dbdto=dto.__dict__
            del dbdto['request']
            del dbdto['vendor']
            data=dbdto|vendor_dto
            serializer=VendorRegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response=serializer.data
                del response['password']
                del response['refresh_token']
                return {"data":response,"info":"vendor is created!","timestamp":datetime.now().timestamp()}
            else:
                raise Exception(str(serializer.errors))
        except Exception as e:
            raise Exception(str(e))