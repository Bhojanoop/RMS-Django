from rest_framework import serializers
from micro_branch_service.models.model import Branch,BranchMeta

class BranchMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model=BranchMeta
        exclude=('branch',)

class BranchSerializer(serializers.ModelSerializer):
    branch_meta=BranchMetaSerializer(many=True,default=[])
    class Meta:
        model=Branch
        fields=(
            'branch_id',
            'branch_name',
            'branch_meta',
            'created_at'
        )