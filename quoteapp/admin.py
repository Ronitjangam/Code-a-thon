from django.contrib import admin
from .models import topic,author,quotemodel

# Register your models here.

admin.site.register(topic)
admin.site.register(author)
admin.site.register(quotemodel)
