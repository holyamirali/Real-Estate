from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="listings"),
    path('<int:listing_id>', details, name="details"),
    #path('search', search, name="search"),
]