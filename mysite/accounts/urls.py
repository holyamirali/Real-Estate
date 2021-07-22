from django.urls import path
from .views import *

urlpatterns = [
    path('register<str:name>', register, name='register'),
    path('<str:name>login', login, name='login'),
    path('<str:name>logout', logout, name='logout')
]