from rest_framework import serializers
from .models import Registration, AddCourseRequest
from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "code", "title", "credit_hours"]

class RegistrationSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)  # nested courses
    student_id = serializers.CharField(source="student.student_id", read_only=True)

    class Meta:
        model = Registration
        fields = "__all__"
        read_only_fields = ("is_paid", "is_approved", "created_at")
class AddCourseRequestSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source="student.student_id", read_only=True)

    class Meta:
        model = AddCourseRequest
        fields = "__all__"
        read_only_fields = ("is_paid", "is_approved", "created_at")
