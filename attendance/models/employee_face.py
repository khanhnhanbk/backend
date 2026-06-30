from django.db import models

from .employee import Employee


class EmployeeFace(models.Model):

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employee_faces"
    )

    # vector for AI models
    face_id = models.CharField(max_length=100, unique=True, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
