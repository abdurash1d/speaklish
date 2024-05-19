from django.urls import path

from . import api_endpoints

app_name = "users"

urlpatterns = [
    path("login/", api_endpoints.LoginView.as_view(), name="login"),
    path("profile-update/", api_endpoints.ProfileUpdateAPIView.as_view(), name="profile_update"),
    path("password-change/", api_endpoints.PasswordChangeAPIView.as_view(), name="password_change"),
    path("user-profile/", api_endpoints.UserProfileRetrieveAPIView.as_view(), name="user_profile"),
]
