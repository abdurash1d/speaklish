from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser

from apps.common.permissions import APIPermission
from apps.users.models import User

from .serializers import TeachersGetUpdateDeleteSerializer


class TeachersGetUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeachersGetUpdateDeleteSerializer
    permission_classes = (APIPermission,)
    parser_classes = [MultiPartParser]
    allowed_roles = ["staff"]

    def get_queryset(self):
        return User.objects.filter(role="teacher", added_by=self.request.user)

    def get_object(self):
        return self.get_queryset().get(id=self.kwargs.get("pk"))


__all__ = ["TeachersGetUpdateDeleteAPIView"]
