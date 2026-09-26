from django.urls import path

from .views import VideoListCreateView, VideoDetailView, WatchHistoryCreateView

urlpatterns = [
    path('',VideoListCreateView.as_view()),
    path('<int:pk>',VideoDetailView.as_view()),
    path('watch-history',WatchHistoryCreateView.as_view(),name='watch-history'),
    path('watch-history/<int:pk>',WatchHistoryCreateView.as_view(), name='delete-watch-history'),

]