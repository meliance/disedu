from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Student
from courses.models import Course
from registrations.models import Registration

User = get_user_model()

# Nested serializer for courses
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'title', 'credit_hours']

# Nested serializer for registrations
class RegistrationNestedSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'terms', 'courses', 'is_paid', 'is_approved', 'created_at']

# Main Student serializer
class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'email',
            'student_id',
            'student_type',
            'program',
            'department',
            'enrollment_year',
            'year',
            'phone',
            'is_approved',
            'is_active',
            'created_at',
        ]
        read_only_fields = ('is_approved', 'is_active')

# Dashboard serializer with nested registrations
class StudentDashboardSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
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
        return RegistrationNestedSerializer(regs, many=True).data
