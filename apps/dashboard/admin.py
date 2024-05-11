# Register your models here.
from django.contrib import admin

from apps.dashboard.models import Group, Organization, StudentTestResult


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "manager"]
    search_fields = ["name", "manager__username"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", "teacher", "start_date", "end_date"]
    search_fields = ["name", "teacher__username"]


@admin.register(StudentTestResult)
class StudentTestResultAdmin(admin.ModelAdmin):
    list_display = ["student", "group", "result"]
    search_fields = ["student__username", "group__name"]
