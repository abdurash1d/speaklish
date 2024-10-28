from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel

from apps.common.models import TimeStampedModel


class Organization(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=255)
    manager = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="organization")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")


class Group(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="teaching_groups")
    start_date = models.DateField()
    end_date = models.DateField()
    referral_link = models.URLField(null=True, blank=True)
    students_count = models.PositiveIntegerField(default=0)
    organization = models.ForeignKey(
        "dashboard.Organization", on_delete=models.PROTECT, related_name="groups", null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")


class StudentTestResult(TimeStampedModel, SoftDeleteModel):
    student = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="test_results")
    group = models.ForeignKey("dashboard.Group", on_delete=models.CASCADE, related_name="test_results")
    result = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.result}"

    class Meta:
        verbose_name = _("Student test result")
        verbose_name_plural = _("Student test results")



# From old db
class ParsedSessions(models.Model):
    id = models.BigAutoField(primary_key=True)
    raw_json = models.TextField()
    parsed_json = models.JSONField()
    feedback = models.TextField()
    band_score = models.DecimalField(max_digits=2, decimal_places=1)
    fluency = models.DecimalField(max_digits=2, decimal_places=1)
    vocabulary = models.DecimalField(max_digits=2, decimal_places=1)
    grammar = models.DecimalField(max_digits=2, decimal_places=1)
    pronunciation = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    used_topic_words = models.JSONField()
    suggested_vocab = models.JSONField()
    wait_time = models.FloatField()
    token_usage = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    session = models.ForeignKey('TestSessionSchools', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parsed_sessions'
        

class TestSessionSchools(models.Model):
    id = models.BigAutoField(primary_key=True)
    result = models.TextField(blank=True, null=True)
    student_id = models.BigIntegerField(blank=True, null=True)
    finish_state = models.CharField(max_length=255, blank=True, null=True)
    stop_reason = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    wait_time = models.IntegerField(blank=True, null=True, db_comment='wait time in request in seconds')
    used_tokens = models.IntegerField(blank=True, null=True)
    is_test = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    school = models.ForeignKey('OLDAuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'test_session_schools'


class SchoolProfiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    session_count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    school = models.OneToOneField('OLDAuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'school_profiles'


class OLDAuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
