from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Organization(TimeStampedModel):
    name = models.CharField(max_length=255)
    manager = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="organizations")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")


class Group(TimeStampedModel):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="teaching_groups")
    start_date = models.DateField()
    end_date = models.DateField()
    referral_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")


class StudentTestResult(TimeStampedModel):
    student = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="test_results")
    group = models.ForeignKey("dashboard.Group", on_delete=models.CASCADE, related_name="test_results")
    result = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.result}"

    class Meta:
        verbose_name = _("Student test result")
        verbose_name_plural = _("Student test results")
