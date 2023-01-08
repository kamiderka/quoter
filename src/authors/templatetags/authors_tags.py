from django import template
from quotes.models import *
from authors.models import Author

register = template.Library()

@register.simple_tag
def count_quotes(author :Author):
    return Quote.objects.filter(author=author).count()


@register.simple_tag
def count_favourite_quotes(author :Author):
    return Quote.objects.filter(author=author, is_fav=True).count()

@register.filter
def has_any_quote(author :Author):
    return Quote.objects.filter(author=author, is_fav=True).count() > 0

@register.simple_tag
def get_authors_works(author :Author):
    return author.source_set.all()
