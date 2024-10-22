from django.apps import AppConfig


class Task2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task2'

    def ready(self):
        import task2.signals