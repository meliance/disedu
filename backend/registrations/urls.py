from django.urls import path
from .views import RoleDashboardView

urlpatterns = [
    path("dashboard/", RoleDashboardView.as_view(), name="role_dashboard"),
]
