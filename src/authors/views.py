from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Author
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic.list import ListView
from quotes.views import QuoteGalleryView
from django.db.models import Count


class AuthorsGalleryView( ListView):
    # login_url = reverse_lazy('login')
    template_name = 'authors_gallery.html'
    context_object_name = 'all_authors_list'

    def get_queryset(self):
        """Returns authors QuerySet<>."""
        
        return Author.objects.exclude(quote=None).order_by('name')  

class SearchAuthorResultsView(AuthorsGalleryView):
    def get_queryset(self):
        query = self.request.GET.get('author')  
        return Author.objects.exclude(quote=None).filter(name__contains=query)
    



