from django import urls
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView, name="blogView"),
    path('no<int:id>', BlogPost, name="blogPost"),
]