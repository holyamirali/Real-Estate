from typing import List
from django.shortcuts import render, get_object_or_404
from .models import Listings

def index(request):
    listings = Listings.objects.all
    context = {
        "listings" : listings
    }
    return render(request, "listings/category_list.html", context=context)

def details(request, listing_id):
    listing = get_object_or_404(Listings, id=listing_id)
    context = {
        "listing" : listing
    }
    return render(request, "listings/single.html", context=context)