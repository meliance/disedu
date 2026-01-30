from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RoleDashboardView

urlpatterns = [
    # JWT login/logout
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Role-based dashboard
    path("dashboard/", RoleDashboardView.as_view(), name="role_dashboard"),
]
