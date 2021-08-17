from django.apps import AppConfig


class TtkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TTK'


    def ready(self):
        import TTK.signals
