from rest_framework import serializers

from apps.dashboard.models import Group
from apps.users.models import User


class GroupSerializerForUserProfile(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "name",
        )


class UserProfileSerializer(serializers.ModelSerializer):
    group = GroupSerializerForUserProfile()

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "role", "phone", "photo", "username", "email", "group")
