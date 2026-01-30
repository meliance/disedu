from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, CourseViewSet, CourseMaterialViewSet

router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("courses", CourseViewSet)
router.register("materials", CourseMaterialViewSet)

urlpatterns = router.urls
