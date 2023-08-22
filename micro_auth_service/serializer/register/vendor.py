from rest_framework import serializers
from micro_auth_service.model.vendor_models import Vendor

class VendorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'