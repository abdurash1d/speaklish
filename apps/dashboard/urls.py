from django.urls import path

from .api_endpoints import staff, teacher

app_name = "dashboard"

urlpatterns = [
    # Staff API Endpoints
    path("staff/teachers/", staff.TeachersListCreateAPIView.as_view(), name="staff_teachers_list_create"),
    path(
        "staff/teachers/<int:pk>/",
        staff.TeachersGetUpdateDeleteAPIView.as_view(),
        name="staff_teachers_get_update_delete",
    ),
    path("staff/groups/", staff.GroupListCreateAPIView.as_view(), name="staff_groups_list_create"),
    path(
        "staff/groups/<int:pk>/",
        staff.GroupGetUpdateDeleteAPIView.as_view(),
        name="staff_groups_get_update_delete",
    ),
    path(
        "staff/groups/students/",
        staff.StudentsListCreateAPIView.as_view(),
        name="staff_students_list_create_create",
    ),
    # Teacher API Endpoints
    path("teacher/groups/", teacher.GroupListCreateAPIView.as_view(), name="teacher_groups_create"),
    path(
        "teacher/groups/<int:pk>/",
        teacher.GroupGetUpdateDeleteAPIView.as_view(),
        name="teacher_groups_get_update_delete",
    ),
    path("teacher/groups/students/", teacher.StudentsListCreateAPIView.as_view(), name="teacher_students_create"),
]
