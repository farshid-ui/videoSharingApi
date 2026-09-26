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

class SubscriptionCancelView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            subscription = Subscription.objects.get(
                pk=pk,
                user=request.user,
            )

        except Subscription.DoesNotExist:
            return Response(
                {'detail': 'Subscription not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        if subscription.status == 'inactive':
            return Response(
                {'detail': 'Subscription is already inactive'},
                status=status.HTTP_400_BAD_REQUEST
            )

        subscription.status = 'inactive'
        subscription.save(update_fields=['status'])

        return Response(
            {
                'message': 'Subscription cancelled successfully',
                'subscription': SubscriptionSerializer(subscription).data,
            },
        )

class SubscriptionRenewView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            subscription = Subscription.objects.get(
                pk=pk,
                user=request.user,
            )

        except Subscription.DoesNotExist:
            return Response(
                {'detail': 'Subscription not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        if subscription.status != 'active':
            return Response(
                {'detail': 'Only active subscriptions can be renewed'},
                status=status.HTTP_400_BAD_REQUEST
            )

        subscription.end_date = subscription.end_date + timedelta(
            days=subscription.plan.duration_days
        )

        subscription.save(update_fields=['end_date'])

        return Response(
            SubscriptionSerializer(subscription).data,
        )