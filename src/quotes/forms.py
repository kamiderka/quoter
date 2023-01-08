from django import forms
from .models import Quote, Author, Source
from django.http import response


class QuoteCreationForm(forms.ModelForm):
    author = forms.CharField(max_length=40)
    source = forms.CharField( max_length=100, required=False)

    class Meta:
        model = Quote
        fields = ['author', 'source', 'content', 'is_fav']

    def clean_author(self):
        author = self.cleaned_data['author']
        if not author:
            raise forms.ValidationError("'Author' field is required.")
        try:
            author_obj = Author.objects.get(name=author) 
        except Author.DoesNotExist:
            author_obj = Author(name=author)
            author_obj.save()
        finally:
            return author_obj

    def clean_source(self):
        title = self.cleaned_data['source']
        author = self.clean_author()
        
        if not title:
            return None
        try:
            source_obj = Source.objects.get(name=title, author=author) 
            print("Source_obtained")
        except Source.DoesNotExist:
            print("Source no exist")
            source_obj = Source.objects.create(name=title, author=author)
            print("saved")
        except Source.MultipleObjectsReturned:
            source_obj = Source.objects.filter(name=title).first()
        except Source.MultipleObjectsReturned:
            raise response.Http404
        
        return source_obj