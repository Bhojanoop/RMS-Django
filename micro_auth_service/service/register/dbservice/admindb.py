from micro_auth_service.serializer.register.admin import AdminRegisterSerializer
from micro_auth_service.DTO.register.dbdto.admindb import AdminDbDTO
from datetime import datetime
from django.db import transaction

class RegisterAdmin:

    def save(self,request:object)->dict:
        try:
            with transaction.atomic():
                dto=AdminDbDTO(request=request)
                admin_dto=dto.admin.__dict__
                del admin_dto['password']
                del admin_dto['confirm_password']
                dbdto=dto.__dict__
                del dbdto['request']
                del dbdto['admin']
                data=dbdto|admin_dto
                serializer=AdminRegisterSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    response=serializer.data
                    del response['password']
                    del response['refresh_token']
                    return {"data":response,"message":"admin is created!","timestamp":datetime.now().timestamp()}
                else:
                    raise Exception(str(serializer.errors))
        except Exception as e:
            raise Exception(str(e))