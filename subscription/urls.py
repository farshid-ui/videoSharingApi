from django.urls import path
from .views import SubscriptionPlanListView, SubscriptionCreateView, SubscriptionCancelView, SubscriptionRenewView

urlpatterns = [
    path('plans/', SubscriptionPlanListView.as_view(), name='plan_list'),
    path('subscribe/', SubscriptionCreateView.as_view(), name='subscribe'),
    path('<int:pk>/cancel/', SubscriptionCancelView.as_view(), name='subscription-cancel'),
    path('<int:pk>/renew/', SubscriptionRenewView.as_view(), name='subscription-renew'),
]