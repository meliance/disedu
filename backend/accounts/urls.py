from django.urls import path
from .views import RoleDashboardView

app_name = "accounts"

urlpatterns = [
    path("dashboard/", RoleDashboardView.as_view(), name="role_dashboard"),
]
