from django.db import models
from django.conf import settings

from authors.models import Author
from uuid import uuid4
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


from django.utils.text import slugify


class Source(models.Model):
    name    = models.TextField(blank=True, max_length=100)
    author  = models.ForeignKey(Author, on_delete=models.CASCADE)    
    slug    = models.SlugField(blank=True, null=True)

    created_by   = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        """Returns Source's name."""
        return self.name

class Quote(models.Model):
    content     = models.TextField()
    author      = models.ForeignKey(Author, on_delete=models.CASCADE)
    source      = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)
    is_fav      = models.BooleanField(default=False)

    pub_date    = models.DateField('date published', auto_now_add=True)
    created_by   = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        """Returns [First 15 characters of content]... | by [Author's name]. """

        content = self.content[:15]
        if len(self.content) > 15:
            content += '...'
        return f'{content} | by {self.author.name}'
    