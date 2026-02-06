"""
Django default apps configuration module
"""
from django.apps import AppConfig


class DefaultConfig(AppConfig):
    """Default app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'music_app'
