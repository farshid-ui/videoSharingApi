from django.db import models

class Video(models.Model):
    required_plan = models.ForeignKey(
        'subscription.SubscriptionPlan',
        on_delete=models.PROTECT,
        related_name='video',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    thumbnail_url = models.URLField()
    duration = models.PositiveIntegerField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class WatchHistory(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='watch_history',
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='watch_history',
    )
    progress = models.PositiveIntegerField()
    watched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.watched_at}'

class Rating(models.Model):

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='rating_history',
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='rating_history',
    )
    score = models.PositiveSmallIntegerField(
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ],
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.video.title} - {self.score}'

class Comment(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='comment_history',
    )
    video = models.ForeignKey(
        'Video',
        on_delete=models.CASCADE,
        related_name='comment_history',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.video.title} - {self.text}'