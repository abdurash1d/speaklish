from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import MultiPartParser

from apps.common.permissions import APIPermission

from .serializers import ProfileUpdateSerializer


class ProfileUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (APIPermission,)
    allowed_roles = ("staff",)

    def get_object(self):
        return self.request.user


__all__ = ["ProfileUpdateAPIView"]
