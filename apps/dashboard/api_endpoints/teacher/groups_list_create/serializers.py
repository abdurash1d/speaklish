from rest_framework import serializers

from apps.dashboard.models import Group


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "name",
            "start_date",
            "end_date",
            "students_count",
        )
        ref_name = "GroupListSerializerForTeacherRole"


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
        extra_kwargs = {
            "teacher": {"read_only": True},
        }
        ref_name = "GroupCreateSerializerForTeacherRole"

    def validate(self, data):
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("End date must be greater than start date")
        return data

    def create(self, validated_data):
        group = Group.objects.create(**validated_data)

        # Generate referral link

        return group
