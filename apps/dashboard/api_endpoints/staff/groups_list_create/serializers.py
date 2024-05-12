from rest_framework import serializers

from apps.dashboard.models import Group
from apps.users.models import User


class GroupListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class GroupListSerializer(serializers.ModelSerializer):
    teacher = GroupListTeacherSerializer()

    class Meta:
        model = Group
        fields = (
            "id",
            "name",
            "teacher",
            "start_date",
            "end_date",
            "students_count",
        )


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "name",
            "teacher",
            "start_date",
            "end_date",
        )

    def validate_teacher(self, value):
        if value.role != User.RoleChoices.TEACHER:
            raise serializers.ValidationError("Teacher role is required")
        return value

    def validate(self, data):
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("End date must be greater than start date")
        return data

    def create(self, validated_data):
        group = Group.objects.create(**validated_data)

        # Generate referral link

        return group
