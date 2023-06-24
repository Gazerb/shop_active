# External Imports

from django.contrib import admin

# Internal Imports
from .models import Favourites


class FavouritesAdmin(admin.ModelAdmin):
    """
    Admin class for the Favourites model.
    """
    list_display = (
        'username',
    )
    search_fields = (
        'username',
    )
    list_filter = (
        'username',
    )
    list_per_page = 20


admin.site.register(Favourites, FavouritesAdmin)
