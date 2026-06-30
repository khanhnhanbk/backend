from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=True, db_index=True)

    full_name = models.CharField(max_length=255)

    department = models.CharField(max_length=255, blank=True)

    position = models.CharField(max_length=255, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_code} - {self.full_name}"
