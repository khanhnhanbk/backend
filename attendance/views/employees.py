from rest_framework import filters

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, Response

from attendance.models import Employee
from attendance.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "employee_code",
        "full_name",
    ]


class EmployeeImportView(APIView):

    def post(self, request):

        file = request.FILES["file"]

        # parse csv

        return Response(
            {
                "created": 0,
                "updated": 0,
                "failed": 0,
            }
        )
