from django import forms
from .models import Quote, Author
from django.core.exceptions import ObjectDoesNotExist


class QuoteCreationForm(forms.ModelForm):
    author = forms.CharField(max_length=40)

    class Meta:
        model = Quote
        fields = ['source', 'author', 'content', 'is_fav']

    def clean_author(self):
        author = self.cleaned_data['author']
        if not author:
            raise forms.ValidationError("'Author' field is required.")
        try:
            author_obj = Author.objects.get(name=author) 
        except ObjectDoesNotExist:
            author_obj = Author(name=author)
            author_obj.save()
        finally:
            return author_obj