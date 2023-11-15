from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import CustomerUser


class CustomerAuthSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomerUser
        fields = ("email", "password")

    def validate(self, attrs):
        if not self.Meta.model.objects.filter(email=attrs["email"]).exists():
            raise ValidationError(("Email or Password not valid"))
        user = self.Meta.model.objects.get(email=attrs["email"])

        if not user.check_password(attrs["password"]):
            raise ValidationError(("Email or Password not valid"))
        attrs["user"] = user
        return attrs
