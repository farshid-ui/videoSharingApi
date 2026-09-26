from django.urls import path

from .views import VideoListCreateView, VideoDetailView, WatchHistoryCreateView, RatingCreateView, VideoRatingView, \
    CommentCreateView, CommentDetailView, VideoLiveUpdateView

urlpatterns = [
    path('',VideoListCreateView.as_view()),
    path('<int:pk>/',VideoDetailView.as_view()),
    path('watch-history/',WatchHistoryCreateView.as_view(),name='watch-history'),
    path('watch-history/<int:pk>/',WatchHistoryCreateView.as_view(), name='delete-watch-history'),
    path('ratings/',RatingCreateView.as_view(),name='ratings'),
    path('ratings/<int:pk>/',VideoRatingView.as_view(),name='video-rating'),
    path('comments/', CommentCreateView.as_view(),name='comments'),
    path('comments/<int:pk>/', CommentDetailView.as_view(),name='comment-detail'),
    path('live-update/<int:pk>/', VideoLiveUpdateView.as_view(),name='video-live-update'),
]