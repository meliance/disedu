from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer
from .permissions import IsAdminOrRegistrar

class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Student, user=self.request.user)

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrRegistrar]

class ApproveStudentView(APIView):
    permission_classes = [IsAdminOrRegistrar]

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.is_approved = True
        student.is_active = True
        student.save()

        return Response({
            "message": "Student approved successfully",
            "student": student.user.full_name
        })
