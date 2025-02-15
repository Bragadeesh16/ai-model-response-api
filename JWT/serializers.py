from .models import *
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "password2",
        ]

    def save(self, **kwargs):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if len(password) < 8:
            raise serializers.ValidationError({"error": "password must be more than 8 character "})

        if password != password2:
            raise serializers.ValidationError({"error": "password does not match"})

        if CustomUser.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({"error": "email id is already exists"})

        account = CustomUser(email=self.validated_data["email"])
        account.set_password(password)
        account.save()

        return account