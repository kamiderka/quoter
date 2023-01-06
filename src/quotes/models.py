from django.db import models
from authors.models import Author
from uuid import uuid4

class Quote(models.Model):
    content     = models.TextField()
    author      = models.ForeignKey(Author, on_delete=models.CASCADE)
    source      = models.CharField(blank=True,  max_length=100)
    is_fav      = models.BooleanField(default=False)
    pub_date    = models.DateField('date published', auto_now_add=True)


    def __str__(self) -> str:
        """Returns [First 15 characters of content]... | by [Author's name]. """

        content = self.content[:15]
        if len(self.content) > 15:
            content += '...'
        return f'{content} | by {self.author.name}'




    
    def __eq__(self, __o: object) -> bool:
        return self.content == __o.content and self.author == __o.author
    
    
    

    
    
