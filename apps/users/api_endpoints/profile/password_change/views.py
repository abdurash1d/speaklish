from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from apps.common.permissions import APIPermission

from .serializers import PasswordChangeSerializer


class PasswordChangeAPIView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (APIPermission,)
    allowed_roles = ("staff",)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        current_password = serializer.validated_data["current_password"]
        new_password = serializer.validated_data["new_password"]

        if not user.check_password(current_password):
            raise ValidationError({"current_password": "Current password is not valid"})

        user.set_password(new_password)
        user.save()

        return Response({"status": "success", "message": "Password successfully changed!"}, status=HTTP_200_OK)


__all__ = ["PasswordChangeAPIView"]
