from django.db import models
from students.models import Student
from courses.models import Course
from payments.models import Payment


class Registration(models.Model):
    TERMS = (
        ("term1", "Term 1"),
        ("term2", "Term 2"),
        ("term3", "Term 3"),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    terms = models.CharField(max_length=20, choices=TERMS)
    courses = models.ManyToManyField(Course, blank=True)

    is_paid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def mark_as_paid(self):
        payment = Payment.objects.filter(
            student=self.student,
            payment_type="registration",
            status="success"
        ).first()

        if payment:
            self.is_paid = True
            self.save()

        return self.is_paid

    def __str__(self):
        return f"{self.student.user.username} — {self.terms}"


class AddCourseRequest(models.Model):
    REASONS = (
        ("f_grade", "F Grade"),
        ("missed_exam", "Missed Exam"),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REASONS)

    is_paid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def mark_as_paid(self):
        payment = Payment.objects.filter(
            student=self.student,
            payment_type="add_course",
            status="success"
        ).first()

        if payment:
            self.is_paid = True
            self.save()

        return self.is_paid

    def __str__(self):
        return f"{self.student.user.username} - {self.course.code}"
