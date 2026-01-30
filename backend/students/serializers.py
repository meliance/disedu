from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

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
            "year",
            "phone",
            "is_approved",
            "is_active",
            "created_at",
        ]
        read_only_fields = ("is_approved", "is_active")
