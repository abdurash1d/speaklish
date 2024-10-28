from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.common.permissions import APIPermission
from apps.dashboard.models import ParsedSessions

from .serializers import ParsedSessionSerializer
from .filters import ParsedSessionFilter


class ParsedSessionListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = ParsedSessionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ParsedSessionFilter
    queryset = ParsedSessions.objects.all()
    allowed_roles = ('teacher', 'admin')
    