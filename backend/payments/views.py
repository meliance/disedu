from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Override create to automatically set student based on JWT user.
        """
        student = request.user.student_profile
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(student=student, status="pending")  # default pending
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """
        Admin / Finance can see all payments; students only see their own.
        """
        user = self.request.user
        if user.role in ["admin", "finance"]:
            return Payment.objects.all()
        return Payment.objects.filter(student=user.student_profile)
