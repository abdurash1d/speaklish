from rest_framework import serializers

from apps.users.models import User


class TeachersListSerializer(serializers.ModelSerializer):
    # total_students = serializers.IntegerField()
    # avg_score = serializers.FloatField()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            # "total_students",
            # "avg_score",
        )


class TeachersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "photo", "password")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "phone": {"required": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["username"] = f"username@{validated_data['phone']}"
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
