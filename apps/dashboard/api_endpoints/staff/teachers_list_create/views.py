from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser

from apps.common.permissions import APIPermission
from apps.users.models import User

from .serializers import TeachersCreateSerializer, TeachersListSerializer


class TeachersListCreateAPIView(ListCreateAPIView):
    permission_classes = [APIPermission]
    serializer_class = TeachersListSerializer
    serializer_map = {
        "GET": TeachersListSerializer,
        "POST": TeachersCreateSerializer,
    }
    parser_classes = [MultiPartParser]
    allowed_roles = ["staff"]

    def get_queryset(self):
        return User.objects.filter(role="teacher", added_by=self.request.user)

    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method, self.serializer_class)

    def perform_create(self, serializer):
        serializer.save(role="teacher", added_by=self.request.user)


__all__ = ["TeachersListCreateAPIView"]
