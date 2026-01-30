from rest_framework import serializers
from .models import Registration, AddCourseRequest
from courses.models import Course


class RegistrationSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        many=True
    )

    class Meta:
        model = Registration
        fields = "__all__"
        read_only_fields = ("is_paid", "is_approved", "created_at")


class AddCourseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCourseRequest
        fields = "__all__"
        read_only_fields = ("is_paid", "is_approved", "created_at")
