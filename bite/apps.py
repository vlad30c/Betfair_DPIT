from django.apps import AppConfig


class BiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bite'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import bite.signals
