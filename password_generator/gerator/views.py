from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# homepage
def home(request):
    return render(request, 'gerator/home.html')


# password page
def password(request):
    return render(request, 'gerator/password.html')
# Create your views here.
