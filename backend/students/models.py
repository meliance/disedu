from django.db import models
from accounts.models import User

class Student(models.Model):

    STUDENT_TYPE_CHOICES = (
        ("new", "New Student"),
        ("continuing", "Continuing Student"),
    )

    PROGRAM_CHOICES = (
        ("distance", "Distance Education"),
        ("extension", "Extension"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    student_type = models.CharField(
        max_length=15,
        choices=STUDENT_TYPE_CHOICES
    )

    program = models.CharField(
        max_length=20,
        choices=PROGRAM_CHOICES
    )

    department = models.CharField(max_length=150)
    enrollment_year = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(default=1)

    phone = models.CharField(max_length=20)

    # 📂 Required Documents
    grade_10_certificate = models.FileField(
        upload_to="students/documents/grade10/",
        null=True,
        blank=True
    )
    grade_12_certificate = models.FileField(
        upload_to="students/documents/grade12/",
        null=True,
        blank=True
    )
    transcript = models.FileField(
        upload_to="students/documents/transcript/",
        null=True,
        blank=True
    )
    id_card = models.FileField(
        upload_to="students/documents/id_card/",
        null=True,
        blank=True
    )
    photo = models.ImageField(
        upload_to="students/photos/",
        null=True,
        blank=True
    )

    # Approval & status
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.department}"
