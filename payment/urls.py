from django.urls import path

from .views import PaymentCreateView, PaymentHistoryView

urlpatterns = [
    path('create/', PaymentCreateView.as_view(), name='payment_create'),
    path('history/', PaymentHistoryView.as_view(), name='payment_history'),
]