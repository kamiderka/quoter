from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import (Quote, Source, Author)


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo_url'] = "https://imgur.com/ueI2pEG.png"
        context['description'] = 'Welcome to Quoter - the center of your inspirations'
        return context

@login_required(login_url="{% url 'login' %}")
def add_quote(request):
    
    if request.method == 'POST':

        if request.POST.get('is_fav') == 'on':
            is_fav = True
        else:
            is_fav = False

        content = request.POST['content']
        author_name = request.POST['author']
        source_name = request.POST.get('source', None)

        quote = Quote(content=content, is_fav=is_fav, created_by=request.user)


        try:
            author = Author.objects.get(name=author_name, created_by=request.user)
        except Author.DoesNotExist:
            author = Author(name=author_name, created_by=request.user)
            author.save()
        quote.author = author

   
   
        try:
            source = Source.objects.get(name=source_name, created_by=request.user)
        except Source.DoesNotExist:
            source = Source(name=source_name, author=author, created_by=request.user)
            source.save()
        quote.source = source

        quote.save()
        return redirect('quotes:add')

    return render(request, 'add_quote.html')


class QuoteGalleryView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'quotes_gallery.html'
    context_object_name = 'quote_list'

    def get_queryset(self):
        """Return all of user's quotes."""
        print(self.request.user)
        return Quote.objects.filter(created_by=self.request.user).order_by('pub_date')
        
class QuotesOfAuthorGalleryView(QuoteGalleryView):

    
    def get_queryset(self):
        """Return Quotes of specific Author."""
        slug = self.kwargs.get('slug', None)

        return get_list_or_404(Quote, author__slug=slug, created_by=self.request.user)
class FavouriteQuotesOfAuthorGalleryView(QuoteGalleryView):

    def get_queryset(self):
        """Return favourite Quotes of specific Author."""
        slug = self.kwargs.get('slug', None)

        return get_list_or_404(Quote, author__slug=slug, is_fav=True, created_by=self.request.user)
class FavouriteQuotesGalleryView(QuoteGalleryView):

    def get_queryset(self):
        """Return all of favourite quotes ."""

        return Quote.objects.filter(is_fav=True, created_by=self.request.user)
class SearchQuoteResultsView(QuoteGalleryView):
    def get_queryset(self):
        query = self.request.GET.get('q')  
        return Quote.objects.filter(content__contains=query, created_by=self.request.user) 
