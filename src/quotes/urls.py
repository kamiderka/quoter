from django.urls import path
from .views import *

app_name = 'quotes'
urlpatterns = [
    path('', QuoteGalleryView.as_view(), name='gallery'), #
    path('add', QuoteCreationView.as_view(), name='add'),
    path('favourite', FavouriteQuotesGalleryView.as_view(), name='favs'),

    path('<slug:slug>', QuotesOfAuthorGalleryView.as_view(), name='of_author'),
    path('<slug:slug>/favourite', FavouriteQuotesOfAuthorGalleryView.as_view(), name='favs_of_author'), #,  {% url 'quotes:add-quote' %}
    path('search/', SearchQuoteResultsView.as_view(), name='search')
    
    # search quote? w/ slug?
]