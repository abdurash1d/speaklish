from django.urls import path

from . import api_endpoints

app_name = "dashboard"

urlpatterns = [
    # Staff API Endpoints
    path("staff/teachers/", api_endpoints.staff.TeachersListCreateAPIView.as_view(), name="staff_teachers_list"),
    path(
        "staff/teachers/<int:pk>/",
        api_endpoints.staff.TeachersGetUpdateDeleteAPIView.as_view(),
        name="staff_teachers_get_update_delete",
    ),
]
