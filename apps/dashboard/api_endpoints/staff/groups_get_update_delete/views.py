from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.permissions import APIPermission
from apps.dashboard.models import Group

from .serializers import GroupsGetUpdateDeleteSerializer


class GroupGetUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [APIPermission]
    serializer_class = GroupsGetUpdateDeleteSerializer
    allowed_roles = ["staff"]

    def get_queryset(self):
        return Group.objects.filter(organization=self.request.user.organization)


__all__ = ["GroupGetUpdateDeleteAPIView"]
