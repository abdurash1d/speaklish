from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel
from apps.users.managers import UserManager


class User(AbstractUser, TimeStampedModel):
    class RoleChoices(models.TextChoices):
        STAFF = "staff", _("Staff")
        TEACHER = "teacher", _("Teacher")
        STUDENT = "student", _("Student")

    role = models.CharField(_("Role"), max_length=50, choices=RoleChoices.choices, null=True)
    phone = PhoneNumberField(_("Phone number"), null=True, blank=True)
    photo = ResizedImageField(_("Photo"), size=[512, 512], upload_to="user_photo/", null=True, blank=True)
    added_by = models.ForeignKey(
        "self", verbose_name=_("Added by"), on_delete=models.SET_NULL, null=True, blank=True, related_name="added_users"
    )
    # group field is used for students only
    group = models.ForeignKey(
        "dashboard.Group",
        verbose_name=_("Group"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students",
    )

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
