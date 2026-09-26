from rest_framework import serializers
from .models import SubscriptionPlan, Subscription

class SubscriptionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPlan
        fields = [
            'id',
            'name',
            'price',
            'description',
            'duration_days',
            'is_active',
        ]

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            'id',
            'plan',
            'end_date',
            'status',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'start_date',
            'end_date',
            'status',
            'created_at',
        ]

    def validate_plan(self, plan):
        if not plan.is_active:
            raise serializers.ValidationError(
                'This subscription plan is not active.'
            )

        return plan