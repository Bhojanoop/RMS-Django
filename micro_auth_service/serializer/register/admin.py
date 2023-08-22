from rest_framework import serializers
from micro_auth_service.model.admin_model import Admin

class AdminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields='__all__'