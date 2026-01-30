from rest_framework import serializers
from .models import Student
from registrations.models import Registration
from courses.models import Course

# Nested serializer for courses
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'title', 'credit_hours']

# Nested serializer for registrations
class RegistrationSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'terms', 'courses', 'is_paid', 'is_approved', 'created_at']

# Dashboard serializer
class StudentDashboardSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    registrations = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "full_name",
            "email",
            "student_id",
            "student_type",
            "program",
            "department",
            "enrollment_year",
            "year",
            "phone",
            "registrations",
        ]

    def get_registrations(self, obj):
        regs = Registration.objects.filter(student=obj)
        return RegistrationSerializer(regs, many=True).data
