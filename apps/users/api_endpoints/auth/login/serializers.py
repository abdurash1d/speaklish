from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.users.models import User


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ["phone", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if "phone" not in attrs and "username" not in attrs:
            raise serializers.ValidationError(
                _("You must provide either phone or username"),
            )

        if "phone" in attrs and "username" in attrs:
            raise serializers.ValidationError(_("You can't use both phone and username"))
        return attrs
