from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated


class APIPermission(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        if is_authenticated:
            if request.user.role not in view.allowed_roles:
                raise PermissionDenied("You are not allowed to perform this action")
            return True
        else:
            return False
