from django.shortcuts import render
import random


# homepage
def home(request):
    return render(request, 'gerator/home.html')


# password page
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('0123456789')
    upp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    spec = list('.-_')

    if request.GET.get('uppercase'):
        characters.extend(upp)

    if request.GET.get('special'):
        characters.extend(spec)

    if request.GET.get('numbers'):
        characters.extend(numbers)

    length = int(request.GET.get('length', 8))

    the_password = ''

    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'gerator/password.html', {'password': the_password})
# Create your views here.
