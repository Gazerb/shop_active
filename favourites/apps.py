# External Imports
from django.apps import AppConfig


class FavouritesConfig(AppConfig):
    """
    A class for configuring the favourites app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favourites'
