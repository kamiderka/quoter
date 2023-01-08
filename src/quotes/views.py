from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView, FormView, TemplateView
from .forms import QuoteCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin



from .models import (Quote)

class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description'] = 'To jest przykładowy opis strony głównej'
        return context

class QuoteCreationView( FormView):
    #login_url = reverse_lazy('login')
    form_class = QuoteCreationForm
    template_name = 'add_quote.html'
    success_url = reverse_lazy('quotes:add')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class QuoteGalleryView( ListView):
    #login_url = reverse_lazy('login')
    template_name = 'quotes_gallery.html'
    context_object_name = 'quote_list'

    def get_queryset(self):
        """Return all of user's quotes."""
        print(self.request.user)
        return Quote.objects.order_by('pub_date')
        
class QuotesOfAuthorGalleryView(QuoteGalleryView):

    
    def get_queryset(self):
        """Return Quotes of specific Author."""
        slug = self.kwargs.get('slug', None)

        return get_list_or_404(Quote, author__slug=slug)
class FavouriteQuotesOfAuthorGalleryView(QuoteGalleryView):

    def get_queryset(self):
        """Return favourite Quotes of specific Author."""
        slug = self.kwargs.get('slug', None)

        return get_list_or_404(Quote, author__slug=slug, is_fav=True)
class FavouriteQuotesGalleryView(QuoteGalleryView):

    def get_queryset(self):
        """Return all of favourite quotes ."""

        return Quote.objects.filter(is_fav=True)
class SearchQuoteResultsView(QuoteGalleryView):
    def get_queryset(self):
        query = self.request.GET.get('q')  
        return Quote.objects.filter(content__contains=query) 
