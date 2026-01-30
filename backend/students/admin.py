from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "student_id",
        "student_type",
        "program",
        "department",
        "year",
        "is_approved",
    )

    list_filter = (
        "student_type",
        "program",
        "department",
        "is_approved",
    )

    search_fields = (
        "user__full_name",
        "user__email",
        "student_id",
    )
