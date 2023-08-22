from rest_framework import serializers
from micro_auth_service.model.customer_model import Customer

class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'