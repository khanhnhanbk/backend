from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from attendance.models import AttendanceEvent
from attendance.serializers import AttendanceEventSerializer


class AttendanceEventViewSet(ModelViewSet):
    queryset = AttendanceEvent.objects.all().order_by("-event_time")
    serializer_class = AttendanceEventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "employee__full_name",
        "employee__employee_code",
        "event_type",
        "source",
    ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
