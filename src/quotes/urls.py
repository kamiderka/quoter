from django.urls import path
from .views import (GalleryView, home_view )

app_name = 'quotes'
urlpatterns = [
    path('', GalleryView.as_view(), name='gallery') #
    #path('', add_quote, name='add-quote'),  {% url 'quotes:add-quote' %}
    #show quotes' gallery 
    #show quote by id  
    # search quote? w/ slug?

    
]