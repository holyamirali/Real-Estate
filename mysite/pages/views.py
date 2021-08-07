from django.shortcuts import render
from .models import About

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    context = {
        'abouts' : About.objects.all
    }
    return render(request, 'pages/about.html', context=context)

def contact(request):
    return render(request, 'pages/contact.html')