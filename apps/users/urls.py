from django.urls import path

from . import api_endpoints

app_name = "users"

urlpatterns = [
    path("login/", api_endpoints.LoginView.as_view(), name="login"),
]
