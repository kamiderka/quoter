"""quoter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from quotes.views import HomePageView
from accounts.views import RegisterView, LoginView, logoutUser
from quotes.api.views import *
from authors.api.views import *

from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, basename='quote')
# router.register(r'authors', AuthorsViewSet, basename='author')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomePageView.as_view(), name="homepage"),
    path('quotes/', include('quotes.urls'), name="quotes"),
    path('authors/', include('authors.urls'), name="authors"),
    # path('api', lambda request: render(request, 'coming_soon.html'), name="api"),

    path('api/', include(router.urls), name="api"),    

    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', logoutUser, name="logout"),
    ]

urlpatterns += staticfiles_urlpatterns()