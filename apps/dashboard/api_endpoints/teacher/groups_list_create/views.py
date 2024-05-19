from rest_framework.generics import ListCreateAPIView

from apps.common.permissions import APIPermission
from apps.dashboard.models import Group

from .serializers import GroupCreateSerializer, GroupListSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    permission_classes = (APIPermission,)
    serializer_class = GroupListSerializer
    search_fields = ("name",)
    serializer_map = {
        "GET": GroupListSerializer,
        "POST": GroupCreateSerializer,
    }
    allowed_roles = ("teacher",)

    def get_queryset(self):
        return Group.objects.filter(teacher=self.request.user)

    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method, self.serializer_class)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(teacher=user, organization=user.added_by.organization)


__all__ = ["GroupListCreateAPIView"]
