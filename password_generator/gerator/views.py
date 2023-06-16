from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random


# homepage
def home(request):
    return render(request, 'gerator/home.html')


# password page
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = 10
    the_password = ''
    for i in range(length):
        the_password += random.choice(characters)
    return render(request, 'gerator/password.html', {'password': the_password})
# Create your views here.
