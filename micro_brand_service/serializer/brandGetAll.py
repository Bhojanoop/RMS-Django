from micro_brand_service.models.brand import Brand
from micro_brand_service.models.brandVerification import BrandVerification
from micro_brand_service.models.brandRoles import BrandRoles
from rest_framework import serializers

class BrandVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=BrandVerification
        fields=('brand_verify_id','govt_doc_filename','user')

class BrandRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=BrandRoles
        exclude = ('brand', )

class BrandGetAllSerializer(serializers.ModelSerializer):
    brand_verification=BrandVerificationSerializer(many=True,default=[])
    brandroles_brand=BrandRoleSerializer(many=True,default=[])
    class Meta:
        model=Brand
        fields=('brand_id','brand_name','brand_name','brand_logo_filename','is_verified','created_at','brand_verification','brandroles_brand')


