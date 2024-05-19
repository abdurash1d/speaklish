from rest_framework import serializers


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(min_length=8, required=True)
    new_password = serializers.CharField(min_length=8, required=True)
