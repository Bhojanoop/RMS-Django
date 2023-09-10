from micro_branch_service.models.model import Branch,BranchMeta
from micro_branch_service.DTO.branch_main_dto.branchCreateDbDto import BranchCreateDbDTO
from django.db import transaction
from micro_branch_service.serializer.getBranch import BranchSerializer

class BranchMainService:

    def create(self,request:object)->dict:
        try:
            print(BranchSerializer(Branch.objects.get(branch_id="c1e2dad5-b2cc-36fe-965c-1d7b836e07e3"),many=False).data)
            _dto=BranchCreateDbDTO(request=request)

            with transaction.atomic():
                branchs=Branch(
                    branch_id=_dto.branch_id,
                    branch_name=_dto.main_dto.branch_name,
                    brand=_dto.brand,
                    created_at=_dto.created_at
                )

                branchs.save()

                branch_meta=BranchMeta(
                    branch_meta_id=_dto.branch_meta_id,
                    branch=branchs,
                    postal_code=_dto.main_dto.postal_code,
                    city=_dto.main_dto.city,
                    state=_dto.main_dto.state,
                    district=_dto.main_dto.district,
                    address_1=_dto.main_dto.address_1,
                    address_2=_dto.main_dto.address_2
                )

                branch_meta.save()
                
                return {"branch":BranchSerializer(branchs,many=False).data,"message":"branch created successfully!"}
        except Exception as e:
            raise Exception(str(e))