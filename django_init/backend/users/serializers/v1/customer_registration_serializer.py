from users.models import CustomerUser
from rest_framework import serializers


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return CustomerUser.objects.create_user(**validated_data, is_active=False)

    class Meta:
        model = CustomerUser
        exclude = (
            "is_active",
            # "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
            "date_joined",
        )
