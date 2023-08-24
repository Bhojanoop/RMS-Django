from micro_brand_service.models.brand import Brand
from rest_framework import serializers

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'