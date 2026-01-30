from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Registration, AddCourseRequest
from .serializers import (
    RegistrationSerializer,
    AddCourseRequestSerializer
)
from .permissions import IsStudent, IsRegistrarOrAdmin


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ["admin", "registrar"]:
            return Registration.objects.all()
        return Registration.objects.filter(student__user=user)

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsStudent()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsRegistrarOrAdmin()]
        return super().get_permissions()


class AddCourseRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AddCourseRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ["admin", "registrar"]:
            return AddCourseRequest.objects.all()
        return AddCourseRequest.objects.filter(student__user=user)

    def get_permissions(self):
        if self.action == "create":
            return [IsStudent()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsRegistrarOrAdmin()]
        return super().get_permissions()
