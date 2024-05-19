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
        ref_name = "StudentsListGroupSerializerForTeacherRole"


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
        ref_name = "StudentsListSerializerForTeacherRole"


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
        ref_name = "StudentsCreateSerializerForTeacherRole"

    def validate_group(self, value):
        if value.teacher != self.context["request"].user:
            raise serializers.ValidationError("This group does not belong to you")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
