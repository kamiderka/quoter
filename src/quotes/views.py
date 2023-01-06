from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from .forms import QuoteCreationForm
from django.urls import reverse_lazy


from .models import (Quote)

def home_view(request):
    return render(request, "homepage.html", {})


class GalleryView(ListView):
    template_name = 'quotes_gallery.html'
    context_object_name = 'all_objects_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Quote.objects.all()


class QuoteCreationView(FormView):
    form_class = QuoteCreationForm
    template_name = 'add_quote.html'
    success_url = reverse_lazy('quotes:add')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)