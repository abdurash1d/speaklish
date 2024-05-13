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
    path("staff/groups/", api_endpoints.staff.GroupListCreateAPIView.as_view(), name="staff_groups_list"),
    path(
        "staff/groups/<int:pk>/",
        api_endpoints.staff.GroupGetUpdateDeleteAPIView.as_view(),
        name="staff_groups_get_update_delete",
    ),
    path(
        "staff/groups/students/",
        api_endpoints.staff.StudentsListCreateAPIView.as_view(),
        name="staff_students_list_create",
    ),
]
