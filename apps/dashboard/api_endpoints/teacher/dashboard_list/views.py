from rest_framework.generics import ListAPIView

from apps.common.permissions import APIPermission
from apps.dashboard.models import ParsedSessions

from .serializers import ParsedSessionSerializer


class ParsedSessionListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = ParsedSessionSerializer
    search_fields = ("session",)
    allowed_roles = ("teacher",)

    def get_queryset(self):
        return ParsedSessions.objects.filter(
            # session__teacher=self.request.user
        ).order_by("-band_score")