from django.contrib import admin
from .models import Registration, AddCourseRequest

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["student", "terms", "is_paid", "is_approved", "created_at"]
    list_filter = ["terms", "is_paid", "is_approved"]
    search_fields = ["student__user__full_name", "student__user__email"]
    filter_horizontal = ["courses"]

@admin.register(AddCourseRequest)
class AddCourseRequestAdmin(admin.ModelAdmin):
    list_display = ["student", "course", "reason", "is_paid", "is_approved", "created_at"]
    list_filter = ["reason", "is_paid", "is_approved"]
    search_fields = ["student__user__full_name", "student__user__email", "course__code"]
