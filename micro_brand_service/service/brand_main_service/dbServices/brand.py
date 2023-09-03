from micro_brand_service.serializer.brandCreate import BrandCreateSerializer
from micro_brand_service.DTO.brand_main_dto.dbdto.brand_db import BrandCreateDbDTO
from micro_brand_service.service.brand_generic_service.create_role_service import CreateRoleService
from micro_brand_service.models.roles import RolesForBrand
from micro_brand_service.DTO.brand_generic_dto.createRole_dto import BrandCreateRoleDTO
from micro_auth_service.model.vendor_models import Vendor
from micro_brand_service.models.brand import Brand

class CreateBrand:

    def _createDefaultRole(self,userid:str,brand_id:str,role_id:str):
        try:
            return CreateRoleService().create(
                BrandCreateRoleDTO(user=Vendor.objects.get(id=userid),brand=Brand.objects.get(brand_id=brand_id),role=RolesForBrand.objects.get(id=role_id))
            )
        except Exception as e:
            raise Exception(str(e))

    def save(self,request:object)->dict:
        try:
            dto=BrandCreateDbDTO(request=request).__dict__

            main_dto=dto['main_dto'].__dict__
            vendor_id=main_dto['userId']
            del dto['request']
            del dto['main_dto']
            del main_dto['userId']
            del main_dto['brand_logo_b64encode']
            del main_dto['govt_doc_filename']
            del main_dto['govt_doc_b64encode']

            data=dto|main_dto

            serializer=BrandCreateSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

                self._createDefaultRole(
                userid=vendor_id,
                brand_id=dto['brand_id'],
                role_id='1B'
                )

                return serializer.data
            
            raise Exception(str(serializer.errors))
        except Exception as e:
            raise Exception(str(e))



