from rest_framework.generics import ListCreateAPIView

from apps.common.permissions import APIPermission
from apps.dashboard.models import Group

from .serializers import GroupCreateSerializer, GroupListSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    permission_classes = [APIPermission]
    serializer_class = GroupListSerializer
    serializer_map = {
        "GET": GroupListSerializer,
        "POST": GroupCreateSerializer,
    }
    allowed_roles = ["staff"]

    def get_queryset(self):
        return Group.objects.filter(organization=self.request.user.organization)

    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method, self.serializer_class)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)


__all__ = ["GroupListCreateAPIView"]
