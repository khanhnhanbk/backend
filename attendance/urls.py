from django.urls import path
from rest_framework.routers import DefaultRouter

from attendance.views.employee_faces import (
    EmployeeFaceDeleteView,
    EmployeeFaceListCreateView,
)
from attendance.views.employees import EmployeeViewSet
from attendance.views.attendance_events import AttendanceEventViewSet

router = DefaultRouter()
router.register("events", AttendanceEventViewSet)
router.register("", EmployeeViewSet)

urlpatterns = router.urls
urlpatterns += [
    path(
        "<int:employee_id>/faces/",
        EmployeeFaceListCreateView.as_view(),
    ),
    path(
        "faces/<int:pk>/",
        EmployeeFaceDeleteView.as_view(),
    ),
]
