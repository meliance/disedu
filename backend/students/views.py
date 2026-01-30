from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentDashboardSerializer
from registrations.models import Registration
from registrations.serializers import RegistrationSerializer
from payments.models import Payment
from payments.serializers import PaymentSerializer
from .permissions import IsAdminOrRegistrar


# ---------- Student Profile ----------
class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentDashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Student, user=self.request.user)


# ---------- Student List ----------
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDashboardSerializer
    permission_classes = [IsAdminOrRegistrar]


# ---------- Approve Student ----------
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


# ---------- Student Dashboard ----------
class StudentDashboardAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        student = get_object_or_404(Student, user=request.user)
        registrations = Registration.objects.filter(student=student)
        payments = Payment.objects.filter(student=student)
        return Response({
            "profile": StudentDashboardSerializer(student).data,
            "registrations": RegistrationSerializer(registrations, many=True).data,
            "payments": PaymentSerializer(payments, many=True).data,
        })
