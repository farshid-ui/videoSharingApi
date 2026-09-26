from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Video, WatchHistory, Rating, Comment
from .serializers import VideoSerializer, WatchHistorySerializer
from .permissions import VideoAccessPermission

class VideoListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        videos = Video.objects.filter(is_published=True)

        serializer = VideoSerializer(videos, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            video = serializer.save()

            return Response(
                VideoSerializer(video).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class VideoDetailView(APIView):

    permission_classes = [IsAuthenticated, VideoAccessPermission]

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)

        except Video.DoesNotExist:
            return Response(
                {'detail': 'Video not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, video)

        serializer = VideoSerializer(video)

        return Response(serializer.data)

    def put(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)

        except Video.DoesNotExist:
            return Response(
                {'detail': 'Video not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VideoSerializer(
            video,
            data=request.data
        )

        if serializer.is_valid():
            video = serializer.save()

            return Response(VideoSerializer(video).data)

        self.check_object_permissions(request, video)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)

        except Video.DoesNotExist:
            return Response(
                {'detail': 'Video not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, video)

        video.delete()

        return Response(
            {'message': 'Video deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

    def patch(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)

        except Video.DoesNotExist:
            return Response(
                {'detail': 'Video not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VideoSerializer(
            video,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            video = serializer.save()

            return Response(VideoSerializer(video).data)

        self.check_object_permissions(request, video)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class WatchHistoryCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None):
        if pk is not None:
            try:
                watch_history = WatchHistory.objects.get(pk=pk, user=request.user)

            except WatchHistory.DoesNotExist:
                return Response(
                    {'detail': 'Watch history not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = WatchHistorySerializer(watch_history)

            return Response(serializer.data)

        watch_history = WatchHistory.objects.filter(user=request.user)

        serializer = WatchHistorySerializer(watch_history, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = WatchHistorySerializer(data=request.data)

        if serializer.is_valid():
            video = serializer.validated_data['video']

            access_permission = VideoAccessPermission()

            if not access_permission.has_object_permission(request, self, video):

                return Response(
                    {'detail': 'You do not have access to this video'},
                    status=status.HTTP_403_FORBIDDEN
                )

            history, created = WatchHistory.objects.update_or_create(
                user=request.user,
                video=video,
                defaults={
                    'progress': serializer.validated_data['progress'],
                }
            )

            return Response(
                WatchHistorySerializer(history).data,
                status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            watch_history = WatchHistory.objects.get(pk=pk, user=request.user)

        except WatchHistory.DoesNotExist:
            return Response(
                {'detail': 'Watch history not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        watch_history.delete()

        return Response(
            {'message': 'Watch history deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

