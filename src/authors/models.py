from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class Author(models.Model):
    slug    = models.SlugField(blank=True, null=True)
    name    = models.CharField(max_length=40)
    is_fav  = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Returns Author's name."""
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)