from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from unfold.forms import (AdminPasswordChangeForm, UserChangeForm,
                          UserCreationForm)

from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "phone", "photo", "group")}),
        (
            "Permissions",
            {"fields": ("role", "added_by", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("id", "username", "email", "phone", "first_name", "last_name", "role")
    list_display_links = ("id", "username")
    readonly_fields = ("last_login", "date_joined", "created_at", "updated_at")
