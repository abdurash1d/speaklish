from rest_framework import serializers

from apps.dashboard.models import Group
from apps.users.models import User


class GroupsDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )
        ref_name = "GroupsDetailTeacherSerializerForTeacherRole"


class GroupsGetUpdateDeleteSerializer(serializers.ModelSerializer):
    teacher = GroupsDetailTeacherSerializer(read_only=True)

    class Meta:
        model = Group
        fields = (
            "id",
            "name",
            "teacher",
            "start_date",
            "end_date",
            "students_count",
            "referral_link",
        )
        extra_kwargs = {
            "referral_link": {"read_only": True},
            "students_count": {"read_only": True},
        }
        ref_name = "GroupsGetUpdateDeleteSerializerForTeacherRole"
