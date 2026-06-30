from rest_framework.generics import DestroyAPIView, ListCreateAPIView

from attendance.models import Employee, EmployeeFace
from attendance.serializers import EmployeeFaceSerializer


class EmployeeFaceListCreateView(ListCreateAPIView):
    serializer_class = EmployeeFaceSerializer

    def get_queryset(self):
        employee_id = self.kwargs["employee_id"]

        return EmployeeFace.objects.filter(employee_id=employee_id)

    def perform_create(self, serializer):
        employee = Employee.objects.get(pk=self.kwargs["employee_id"])

        serializer.save(employee=employee)


class EmployeeFaceDeleteView(DestroyAPIView):
    queryset = EmployeeFace.objects.all()
    serializer_class = EmployeeFaceSerializer
