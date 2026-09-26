from django.urls import path
from .views import SubscriptionPlanListView, SubscriptionCreateView

urlpatterns = [
    path('plans/', SubscriptionPlanListView.as_view(), name='plan_list'),
    path('subscribe/', SubscriptionCreateView.as_view(), name='subscribe'),
]