from django import forms
from .models import Registration, AddCourseRequest

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["student", "terms", "courses", "is_paid", "is_approved"]

class AddCourseRequestForm(forms.ModelForm):
    class Meta:
        model = AddCourseRequest
        fields = ["student", "course", "reason", "is_paid", "is_approved"]
