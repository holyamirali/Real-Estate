from django.shortcuts import render, redirect
from django.contrib import auth

def dashboard(request):
    return render(request, "cp/dashboard.html")

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'pages/index.html')
    else:
        return render(request, 'pages/index.html')