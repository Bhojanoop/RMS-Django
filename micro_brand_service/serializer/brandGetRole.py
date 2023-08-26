from micro_brand_service.models.brandRoles import BrandRoles
from rest_framework import serializers

class BrandCreateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=BrandRoles
        fields='__all__'