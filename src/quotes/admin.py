from django.contrib import admin
from .models import (Author, Quote, Source)

# Register your models here.

admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(Source)
