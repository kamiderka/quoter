from django.db import models
from authors.models import Author
from uuid import uuid4

class Quote(models.Model):
    title       = models.CharField(blank=True,  max_length=150)
    content     = models.TextField()
    author      = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_fav      = models.BooleanField(default=False)
    pub_date    = models.DateField('date published', auto_now_add=True)


    def __str__(self) -> str:
        """Returns [Quote's Title] | by [Author's name]. """

        if self.title == None or self.title == "":
            return "[No Title] | by " + str(self.author)

        return self.title + " | by " + str(self.author)


    
    
