from rest_framework import viewsets, permissions
from .models import Department, Course, CourseMaterial
from .serializers import (
    DepartmentSerializer,
    CourseSerializer,
    CourseMaterialSerializer
)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ["admin", "registrar"]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related("department").all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]


class CourseMaterialViewSet(viewsets.ModelViewSet):
    queryset = CourseMaterial.objects.select_related("course").all()
    serializer_class = CourseMaterialSerializer
    permission_classes = [IsAdminOrReadOnly]
