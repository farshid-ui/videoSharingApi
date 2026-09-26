from django.utils import timezone

from rest_framework.permissions import BasePermission

class VideoAccessPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        # Free plan
        if obj.required_plan is None:
            return True

        # User must be authenticated
        if not request.user.is_authenticated:
            return False

        # Check active subscription
        subscription = request.user.subscriptions.filter(
            status='active',
            end_date__gte=timezone.now(),
            plan=obj.required_plan
        ).first()

        return subscription is not None