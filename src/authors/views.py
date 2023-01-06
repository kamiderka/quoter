from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Author

from django.views.generic.list import ListView


class AuthorsGalleryView(ListView):
    template_name = 'authors_gallery.html'
    context_object_name = 'all_objects_list'

    def get_queryset(self):
        """Returns authors QuerySet<>."""
        return Author.objects.all()



