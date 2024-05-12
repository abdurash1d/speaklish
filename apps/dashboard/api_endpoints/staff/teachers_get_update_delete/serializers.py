from rest_framework import serializers

from apps.users.models import User


class TeachersGetUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "photo",
            "password",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": False,
            },
        }

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        super().update(instance, validated_data)
        if password:
            instance.set_password(password)
        return instance
