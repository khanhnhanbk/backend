from django.db import models

from .employee import Employee
from authentication.models import User


class AttendanceEvent(models.Model):

    CHECK_IN = "check_in"
    CHECK_OUT = "check_out"

    EVENT_CHOICES = [
        (CHECK_IN, "Check In"),
        (CHECK_OUT, "Check Out"),
    ]

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="attendance_events"
    )

    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)

    event_time = models.DateTimeField()

    source = models.CharField(max_length=20)

    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )

    created_at = models.DateTimeField(auto_now_add=True)
