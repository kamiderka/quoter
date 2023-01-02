from django.urls import path
from .views import *

app_name = 'authors'
urlpatterns = [
    path('', name='home-view'), # authors' gallery 
    #show author by id w/ slug 
    # search authors? w/ slug? 
    
]