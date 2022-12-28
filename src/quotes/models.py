from django.db import models

class Author(models.Model):
    name    = models.CharField(max_length=40)
    is_fav  = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Returns Author's name."""
        return self.name

class Source(models.Model):
    source  = models.CharField(max_length=80)

    def __str__(self) -> str:
        """Returns source of Quote"""
        return self.source

class Quote(models.Model):
    title       = models.CharField(null=True, blank=True,  max_length=150)
    content     = models.TextField()
    author      = models.ForeignKey(Author, on_delete=models.CASCADE)
    source      = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)
    is_fav      = models.BooleanField(default=False)
    pub_date    = models.DateField('date published')


    def __str__(self) -> str:
        """Returns [Quote's Title] | by [Author's name]. """

        if self.title == None or self.title == "":
            return "[No Title] | by " + str(self.author)

        return self.title + " | by " + str(self.author)

