from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # import signals cause django docs advice to do this in this way cause some import issues
    def ready(self):
        import users.signals