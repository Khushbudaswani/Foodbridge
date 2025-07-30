from django.apps import AppConfig


class VolunteersConfig(AppConfig):
    """
    Configuration class for the 'volunteers' app.

    This class provides metadata and default configurations used by Django
    to set up and manage the 'volunteers' app within the project.
    """
    # Specifies the type of primary key to use by default for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'volunteers'
