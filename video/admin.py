from django.contrib import admin
from .models import Video, WatchHistory, Rating, Comment

admin.site.register(Video)
admin.site.register(WatchHistory)
admin.site.register(Rating)
admin.site.register(Comment)
