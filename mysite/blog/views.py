from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def BlogView(request):
    return HttpResponse("<h1>Here is the main blog view!<h1>")

def BlogPost(request, id):
    return HttpResponse("<h1>We're at post number " + str(id) + " already!<h1>")