from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/subscription/', include('subscription.urls')),
    path('api/payment/', include('payment.urls')),
    path('api/video/', include('video.urls')),
]
