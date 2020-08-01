
from django.contrib import admin
from django.urls import path
from quoteapp import views as v

urlpatterns = [
    path('',v.quotes),
    path('author',v.authors),
    path('topic',v.topics),
    path('quotesonauthor',v.quoteauthor),
    path('quotesontopic',v.quotetopic)
]
