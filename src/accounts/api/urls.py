from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include


router = DefaultRouter()
router.register(r'accounts', )

urlpatterns = [
    path('api/', include(router.urls)),
]