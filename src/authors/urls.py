from django.urls import path
from .views import *

app_name = 'authors'
urlpatterns = [
    path('', AuthorsGalleryView.as_view(), name="gallery"), # authors' gallery 
    path('search/', SearchAuthorResultsView.as_view(), name='search')
    
    #show author by id w/ slug 
    # search authors? w/ slug? 
    
]