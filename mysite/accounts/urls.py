from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('', dashboard, name='dashboard'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
]