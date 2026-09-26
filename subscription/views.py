from django.utils.autoreload import ensure_echo_on
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import SubscriptionPlan, Subscription
from .serializers import SubscriptionPlanSerializer, SubscriptionSerializer

from django.utils import timezone
from datetime import timedelta


class SubscriptionPlanListView(APIView):

    def get(self, request):
        plans = SubscriptionPlan.objects.filter(is_active=True)
        serializer = SubscriptionPlanSerializer(plans, many=True)

        return Response(serializer.data)

class SubscriptionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)

        if serializer.is_valid():
            plan = serializer.validated_data['plan']

            start_date = timezone.now()
            end_date = start_date + timedelta(days=plan.duration_days)

            subscription = Subscription.objects.create(
                user=request.user,
                plan=plan,
                start_date=start_date,
                end_date=end_date,
                status='active',
            )

            return Response(
                SubscriptionSerializer(subscription).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )