from django.apps import AppConfig


class CasualsConfig(AppConfig):
    name = 'casuals'
    
    def ready(self):
        import casuals.signals