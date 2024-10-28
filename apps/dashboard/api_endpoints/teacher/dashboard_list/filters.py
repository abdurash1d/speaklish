from django_filters import rest_framework as filters
from apps.dashboard.models import ParsedSessions


class ParsedSessionFilter(filters.FilterSet):
    student_id = filters.NumberFilter(field_name="session__student_id")
    band_score = filters.NumberFilter()
    band_score__gte = filters.NumberFilter(field_name="band_score", lookup_expr="gte")
    band_score__lte = filters.NumberFilter(field_name="band_score", lookup_expr="lte")
    fluency__gte = filters.NumberFilter(field_name="fluency", lookup_expr="gte")
    fluency__lte = filters.NumberFilter(field_name="fluency", lookup_expr="lte")
    created_at__date = filters.DateFilter(field_name="created_at", lookup_expr="date")
    created_at__date_gte = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    created_at__date_lte = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = ParsedSessions
        fields = []
