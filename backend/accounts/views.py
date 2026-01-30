# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from students.models import Student
from registrations.models import Registration
from payments.models import Payment
from students.serializers import StudentDashboardSerializer
from registrations.serializers import RegistrationSerializer
from payments.serializers import PaymentSerializer


class RoleDashboardView(APIView):
    """
    Returns dashboard data depending on the user's role:
    - Student: profile + registrations + payments
    - Admin / Registrar / Finance: summary stats
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        role = user.role
        data = {"role": role}

        if role == "student":
            # Student dashboard
            student = get_object_or_404(Student, user=user)
            registrations = Registration.objects.filter(student=student)
            payments = Payment.objects.filter(student=student)

            data.update({
                "profile": StudentDashboardSerializer(student).data,
                "registrations": RegistrationSerializer(registrations, many=True).data,
                "payments": PaymentSerializer(payments, many=True).data,
            })

        elif role in ["admin", "registrar", "finance"]:
            # Admin/Registrar/Finance dashboard (summary stats)
            data.update({
                "total_students": Student.objects.count(),
                "pending_approvals": Student.objects.filter(is_approved=False).count(),
                "total_registrations": Registration.objects.count(),
                "pending_registrations": Registration.objects.filter(is_approved=False).count(),
                "total_payments": Payment.objects.count(),
                "pending_payments": Payment.objects.filter(status="pending").count(),
            })

        else:
            data["message"] = "Role not recognized"

        return Response(data)
