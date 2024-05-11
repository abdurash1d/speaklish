from rest_framework import serializers

from apps.users.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone", "password"]
        extra_kwargs = {"password": {"write_only": True}}
