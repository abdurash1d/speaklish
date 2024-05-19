from rest_framework.generics import RetrieveAPIView

from apps.common.permissions import APIPermission

from .serializers import UserProfileSerializer


class UserProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (APIPermission,)
    allowed_roles = ("staff",)

    def get_object(self):
        return self.request.user


__all__ = ["UserProfileRetrieveAPIView"]
