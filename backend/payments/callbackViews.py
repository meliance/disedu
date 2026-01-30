import requests
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Payment
from registrations.models import Registration, AddCourseRequest


CHAPA_VERIFY_URL = "https://api.chapa.co/v1/transaction/verify/"


@api_view(["GET"])
@permission_classes([AllowAny])  # Chapa servers are not authenticated
def chapa_callback(request):
    """
    Chapa redirects here after payment
    """
    tx_ref = request.GET.get("tx_ref")

    if not tx_ref:
        return Response({"error": "Transaction reference missing"}, status=400)

    try:
        payment = Payment.objects.get(reference=tx_ref)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=404)

    # 🔐 Verify with Chapa
    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
    }

    response = requests.get(
        f"{CHAPA_VERIFY_URL}{tx_ref}",
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        payment.status = "failed"
        payment.save()
        return Response({"error": "Verification failed"}, status=400)

    data = response.json()

    if data.get("status") != "success":
        payment.status = "failed"
        payment.save()
        return Response({"error": "Payment not successful"}, status=400)

    # ✅ Payment successful
    payment.status = "success"
    payment.save()

    # 🔁 Update related models
    if payment.payment_type == "registration":
        Registration.objects.filter(
            student=payment.student,
            is_paid=False
        ).update(is_paid=True)

    elif payment.payment_type == "add_course":
        AddCourseRequest.objects.filter(
            student=payment.student,
            is_paid=False
        ).update(is_paid=True)

    return Response({
        "message": "Payment verified successfully",
        "reference": tx_ref,
        "status": "success"
    })
