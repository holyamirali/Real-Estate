from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

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
            return redirect('index')
    else:
        return redirect('index')

def register(request):
    print("REGISTER IS CLICKED")
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if (password != repassword):
            print("Passwords doesnt match")
            return redirect('index')
        if len(password)<8:
            print("Password is short!")
            return redirect('index')
        if User.objects.filter(username=username).exists():
            print("Username exists! new")
            return redirect('index')
        if User.objects.filter(email=email).exists():
            print("Email exists!")
            return redirect('index')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = auth.authenticate(username=username, password=password)
        print("Hmmm everything correct!!")
        return redirect('dashboard')
    else:
        return redirect('index')