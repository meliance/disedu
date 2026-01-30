from rest_framework import serializers
from .models import Payment
from students.models import Student

class PaymentSerializer(serializers.ModelSerializer):
    student_email = serializers.CharField(source="student.user.email", read_only=True)
    student_full_name = serializers.CharField(source="student.user.full_name", read_only=True)

    class Meta:
        model = Payment
        fields = [
            "id",
            "student",
            "student_email",
            "student_full_name",
            "amount",
            "reference",
            "payment_type",
            "status",
            "created_at",
        ]
        read_only_fields = ["status", "created_at"]
