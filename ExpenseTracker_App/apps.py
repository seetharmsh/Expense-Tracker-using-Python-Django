from django.apps import AppConfig


class ExpensetrackerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ExpenseTracker_App'

    def ready(self):
        import ExpenseTracker_App.signals