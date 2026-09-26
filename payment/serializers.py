from rest_framework import serializers

from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Payment

        fields = [
            'id',
            'subscription',
            'amount',
            'status',
            'created_at',
            'paid_at',
        ]

        read_only_fields = [
            'id',
            'amount',
            'status',
            'created_at',
            'paid_at',
        ]