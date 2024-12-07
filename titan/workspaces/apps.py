from django.apps import AppConfig
from django.db.models.signals import post_save


class WorkspacesConfig(AppConfig):
    name = "titan.workspaces"

    def ready(self):
        from titan.workspaces import signals
        from titan.users.models import User

        post_save.connect(signals.create_default_workspace, sender=User)
