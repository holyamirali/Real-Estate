from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="listings"),
    #path('cat<int:id>', singleCat, name="singleCat"),
    #path('search', search, name="search"), 
]