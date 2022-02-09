from django.apps import AppConfig

class AuthConfig(AppConfig):
    name = 'apps.auth'
    label = 'apps_auth'
    def ready(self):
        print('masuk authentication signals')
        import authentication.signals

# class UsersConfig(AppConfig):
#     name = 'users'
  
