from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import (
    RegisterView,
    MeView,
    RoleDashboardView,
)

app_name = "accounts"

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", MeView.as_view(), name="me"),
    path("dashboard/", RoleDashboardView.as_view(), name="role_dashboard"),
]

urlpatterns += router.urls
