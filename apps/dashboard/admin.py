# Register your models here.
from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.dashboard.models import Group, Organization, StudentTestResult


@admin.register(Organization)
class OrganizationAdmin(ModelAdmin):
    list_display = ["name", "manager"]
    search_fields = ["name", "manager__username"]


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ["name", "teacher", "start_date", "end_date"]
    search_fields = ["name", "teacher__username"]


@admin.register(StudentTestResult)
class StudentTestResultAdmin(ModelAdmin):
    list_display = ["student", "group", "result"]
    search_fields = ["student__username", "group__name"]
