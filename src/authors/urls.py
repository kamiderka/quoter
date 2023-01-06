from django.urls import path
from .views import *

app_name = 'authors'
urlpatterns = [
    path('', AuthorsGalleryView.as_view(), name="qallery"), # authors' gallery 
    #show author by id w/ slug 
    # search authors? w/ slug? 
    
]