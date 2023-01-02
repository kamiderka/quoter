from django.db import models
from authors.models import Author

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
    pub_date    = models.DateField('date published', auto_now_add=True)


    def __str__(self) -> str:
        """Returns [Quote's Title] | by [Author's name]. """

        if self.title == None or self.title == "":
            return "[No Title] | by " + str(self.author)

        return self.title + " | by " + str(self.author)

    
    def is_valid(self):
        pass

    def save(self):
        pass
    
    
