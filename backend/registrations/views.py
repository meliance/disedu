from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404

from students.models import Student
from registrations.models import Registration, AddCourseRequest
from registrations.serializers import RegistrationSerializer, AddCourseRequestSerializer
from accounts.models import User

class RoleDashboardView(APIView):
    """
    Role-based dashboard:
    - Student: see their profile, registrations, and add-course requests
    - Admin/Registrar: see stats and all registrations/add-course requests
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role == "student":
            # Student dashboard
            student = get_object_or_404(Student, user=user)
            registrations = Registration.objects.filter(student=student)
            add_course_requests = AddCourseRequest.objects.filter(student=student)

            return Response({
                "role": "student",
                "profile": {
                    "full_name": user.full_name,
                    "email": user.email,
                    "student_id": student.student_id,
                    "program": student.program,
                    "department": student.department,
                    "year": student.year,
                    "is_approved": student.is_approved,
                    "is_active": student.is_active
                },
                "registrations": RegistrationSerializer(registrations, many=True).data,
                "add_course_requests": AddCourseRequestSerializer(add_course_requests, many=True).data
            })

        elif user.role in ["admin", "registrar"]:
            # Admin/Registrar dashboard stats
            total_students = Student.objects.count()
            total_registrations = Registration.objects.count()
            total_add_course_requests = AddCourseRequest.objects.count()
            pending_registrations = Registration.objects.filter(is_approved=False).count()
            pending_add_course_requests = AddCourseRequest.objects.filter(is_approved=False).count()

            return Response({
                "role": user.role,
                "stats": {
                    "total_students": total_students,
                    "total_registrations": total_registrations,
                    "total_add_course_requests": total_add_course_requests,
                    "pending_registrations": pending_registrations,
                    "pending_add_course_requests": pending_add_course_requests
                }
            })

        else:
            return Response({"detail": "Role not recognized."}, status=status.HTTP_403_FORBIDDEN)
