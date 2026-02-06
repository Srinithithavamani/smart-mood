from django.contrib import admin
from .models import UserProfile, Song, PlaylistHistory, UserPreferences

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_language', 'created_at')
    list_filter = ('preferred_language',)
    search_fields = ('user__username',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'mood', 'language', 'youtube_id')
    list_filter = ('mood', 'language')
    search_fields = ('title', 'artist', 'youtube_id')

@admin.register(PlaylistHistory)
class PlaylistHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'emotion_detected', 'played_at')
    list_filter = ('emotion_detected', 'played_at')
    search_fields = ('user__username', 'song__title')

@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_moods')
    search_fields = ('user__username',)
