from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentDashboardSerializer

class StudentDashboardAPIView(APIView):
    """
    Returns the dashboard info for the logged-in student,
    including profile, registrations, and courses.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        student = get_object_or_404(Student, user=request.user)
        serializer = StudentDashboardSerializer(student)
        return Response(serializer.data)
