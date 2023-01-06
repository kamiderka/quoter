from django.urls import path
from .views import (GalleryView, home_view, QuoteCreationView )

app_name = 'quotes'
urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'), #
    path('add', QuoteCreationView.as_view(), name='add') #,  {% url 'quotes:add-quote' %}
    #show quotes' gallery 
    #show quote by id  
    # search quote? w/ slug?

    
]