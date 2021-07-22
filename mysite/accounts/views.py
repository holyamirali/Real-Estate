from django.shortcuts import render
from django.http import HttpResponse

def register(request, name):
    return HttpResponse("<h1>Welcome sir " + str(name) + "! So lucky to have you ;)<h1>")

def login(request, name):
    return HttpResponse("<h3>Yo " + str(name) + "! How you doin' bro?<h3>")

def logout(request, name):
    return HttpResponse("And I tell you all about it when I see you again, " + str(name) + " !")