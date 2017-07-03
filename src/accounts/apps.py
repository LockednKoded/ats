from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'User Accounts & Profiles'

    def ready(self):
        from . import signals
