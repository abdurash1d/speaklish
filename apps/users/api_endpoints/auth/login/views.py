from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User

from .serializers import LoginSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data.get("phone")
        username = serializer.validated_data.get("username")

        if phone:
            user = User.objects.filter(phone=phone).first()
            if user is None:
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            username = user.username

        user = authenticate(username=username, password=serializer.validated_data.get("password"))

        if user is None:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response(
            {
                "role": user.role,
                "re fresh": refresh_token,
                "access": access_token,
            },
            status=status.HTTP_200_OK,
        )


__all__ = ["LoginView"]
