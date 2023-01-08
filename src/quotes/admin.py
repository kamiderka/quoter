from django.contrib import admin
from .models import ( Quote, Source )

# Register your models here.

admin.site.register(Quote)
admin.site.register(Source)