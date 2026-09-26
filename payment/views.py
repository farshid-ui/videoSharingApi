from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions

from .models import Payment
from .serializers import PaymentSerializer

class PaymentCreateView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            subscription = serializer.validated_data['subscription']

            if subscription.user != request.user:
                return Response(
                    {'detail': 'You cannot pay for another user subscription'},
                    status=status.HTTP_403_FORBIDDEN
                )

            amount = subscription.plan.price

            payment = Payment.objects.create(
                subscription = subscription,
                amount = amount,
                status = 'success',
                paid_at = timezone.now()
            )

            return Response(
                PaymentSerializer(payment).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PaymentHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.filter(
            subscription__user=request.user
        ).order_by('-created_at')

        serializer = PaymentSerializer(payments, many=True)

        return Response(serializer.data)