from micro_brand_service.models.brandVerification import BrandVerification
from rest_framework import serializers


class BrandVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model=BrandVerification
        fields='__all__'