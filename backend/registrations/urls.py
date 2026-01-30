from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet, AddCourseRequestViewSet

router = DefaultRouter()
router.register("registrations", RegistrationViewSet, basename="registrations")
router.register("add-course-requests", AddCourseRequestViewSet, basename="add-course")

urlpatterns = router.urls
