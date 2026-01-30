from django import forms
from .models import Department, Course, CourseMaterial

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "code", "is_active"]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["department", "code", "title", "credit_hours", "description", "is_active"]

class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = ["title", "file"]