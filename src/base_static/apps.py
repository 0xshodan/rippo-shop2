from django.apps import AppConfig


class BaseStaticConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_static'
