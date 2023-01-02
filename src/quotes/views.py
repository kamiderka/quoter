from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import (Quote)

def home_view(request):
    return render(request, "add_quote.html", {})


class GalleryView(generic.ListView):
    template_name = 'gallery.html'
    context_object_name = 'all_quotes_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Quote.objects.all()