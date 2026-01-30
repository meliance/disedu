from django.urls import path
from .views import (
    StudentProfileView,
    StudentListView,
    ApproveStudentView,
)

app_name = "students"

urlpatterns = [
    path("me/", StudentProfileView.as_view(), name="my-profile"),
    path("", StudentListView.as_view(), name="student-list"),
    path("<int:pk>/approve/", ApproveStudentView.as_view(), name="approve-student"),
]
