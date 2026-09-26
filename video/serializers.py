from rest_framework import serializers

from .models import Video, WatchHistory, Rating, Comment

class VideoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Video

        fields = [
            'id',
            'required_plan',
            'title',
            'description',
            'video_url',
            'thumbnail_url',
            'duration',
            'is_published',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

class WatchHistorySerializer(serializers.ModelSerializer):

    class Meta:

        model = WatchHistory

        fields = [
            'id',
            'video',
            'progress',
            'watched_at',
        ]

        read_only_fields = [
            'id',
            'watched_at',
        ]