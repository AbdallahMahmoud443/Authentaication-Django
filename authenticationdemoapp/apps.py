from django.apps import AppConfig


class AuthenticationdemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticationdemoapp'
    #! Important for signals working 
    def ready(self): 
        import authenticationdemoapp.signals 
