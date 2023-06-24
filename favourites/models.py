# External Imports
from django.db import models
from django.contrib.auth.models import User

# Internal Imports:
from products.models import Product


class Favourites(models.Model):
    """
    This model is for a users favourites list
    """
    class Meta:
        verbose_name_plural = 'Favourites'

    products = models.ManyToManyField(
        Product,
        blank=True
    )
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Return object string
        Args:
            self (object): self object.
        Returns:
            str: users favourite string
        """
        return f"{self.username}'s Favourites"
