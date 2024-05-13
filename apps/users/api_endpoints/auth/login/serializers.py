from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    phone = PhoneNumberField(required=False)
    password = serializers.CharField()

    def validate(self, attrs):
        if "phone" not in attrs and "username" not in attrs:
            raise serializers.ValidationError(
                _("You must provide either phone or username"),
            )

        if "phone" in attrs and "username" in attrs:
            raise serializers.ValidationError(_("You can't use both phone and username"))
        return attrs
