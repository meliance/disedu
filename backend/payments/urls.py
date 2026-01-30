from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet
from .callbackViews import chapa_callback

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payment")

urlpatterns = [
    path("", include(router.urls)),
    path("chapa/callback/", chapa_callback, name="chapa-callback"),
]
