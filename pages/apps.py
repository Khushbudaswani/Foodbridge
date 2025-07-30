from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    Configuration class for the 'pages' app.

    This class is used by Django to configure some of the 
    attributes of the application like its name and default 
    primary key field type.
    """
    # Sets the default type of auto-generated primary keys to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
     # Name of the Django app
    name = 'pages'
