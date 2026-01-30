from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student", "payment_type", "amount", "status", "created_at")
    list_filter = ("status", "payment_type", "created_at")
    search_fields = ("student__user__username", "reference")
    readonly_fields = ("created_at", "reference")  # Reference is generated automatically
