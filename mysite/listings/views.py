from django.shortcuts import render
from .models import Listings

def index(request):
    context = {
        "listings" : Listings.objects.all
    }
    return render(request, "listings/category_list.html", context=context)
