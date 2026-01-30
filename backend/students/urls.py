from django.urls import path
from .views import (
    StudentProfileView,
    StudentListView,
    ApproveStudentView,
    StudentDashboardAPIView
)

app_name = "students"

urlpatterns = [
    path("profile/", StudentProfileView.as_view(), name="student_profile"),
    path("list/", StudentListView.as_view(), name="student_list"),
    path("approve/<int:pk>/", ApproveStudentView.as_view(), name="approve_student"),
    path("dashboard/", StudentDashboardAPIView.as_view(), name="student_dashboard"),
]
