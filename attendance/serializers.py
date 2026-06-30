from rest_framework import serializers

from attendance.models import Employee, EmployeeFace, AttendanceEvent


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFace
        fields = "__all__"


class AttendanceEventSerializer(serializers.ModelSerializer):
    employee_name = serializers.ReadOnlyField(source="employee.full_name")
    employee_code = serializers.ReadOnlyField(source="employee.employee_code")
    created_by_email = serializers.ReadOnlyField(source="created_by.email")

    class Meta:
        model = AttendanceEvent
        fields = [
            "id",
            "employee",
            "employee_name",
            "employee_code",
            "event_type",
            "event_time",
            "source",
            "created_by",
            "created_by_email",
            "created_at",
        ]
        read_only_fields = ["created_by", "created_at"]

