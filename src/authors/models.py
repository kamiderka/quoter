from django.db import models
from django.utils.text import slugify
from django_currentuser.db.models import CurrentUserField
from django.contrib.auth.models import User



class Author(models.Model):
    slug        = models.SlugField(blank=True, null=True)
    name        = models.CharField(max_length=40)
    is_fav      = models.BooleanField(default=False)
    
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Returns Author's name."""
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)