from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.permissions import APIPermission
from apps.dashboard.models import Group

from .serializers import GroupsGetUpdateDeleteSerializer


class GroupGetUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (APIPermission,)
    serializer_class = GroupsGetUpdateDeleteSerializer
    allowed_roles = ("teacher",)

    def get_queryset(self):
        return Group.objects.filter(teacher=self.request.user)


__all__ = ["GroupGetUpdateDeleteAPIView"]
