from rest_framework.generics import ListCreateAPIView

from apps.common.permissions import APIPermission
from apps.users.models import User
from .serializers import StudentsListSerializer, StudentsCreateSerializer


class StudentsListCreateAPIView(ListCreateAPIView):
    permission_classes = (APIPermission,)
    serializer_class = StudentsListSerializer
    serializer_map = {
        "GET": StudentsListSerializer,
        "POST": StudentsCreateSerializer,
    }
    allowed_roles = ["staff"]

    def get_queryset(self):
        return User.objects.filter(role="student", group__organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(role="student", added_by=self.request.user)

    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method, self.serializer_class)


__all__ = ["StudentsListCreateAPIView"]
