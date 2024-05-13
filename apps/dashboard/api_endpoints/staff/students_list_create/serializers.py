from rest_framework import serializers

from apps.dashboard.models import Group
from apps.users.models import User


class StudentsListGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "name",
        )


class StudentsListSerializer(serializers.ModelSerializer):
    group = StudentsListGroupSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "username",
            "group",
        )


class StudentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "username",
            "password",
            "group",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
