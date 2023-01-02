from django.db import models

class Author(models.Model):
    name    = models.CharField(max_length=40)
    is_fav  = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Returns Author's name."""
        return self.name