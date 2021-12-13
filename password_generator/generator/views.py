from django.http import HttpResponse
from django.shortcuts import render
import random
import string


# Create your views here.

def home(request):
    return render(request, 'generator/index.html')


def password(request):
    the_password = ''
    characters = list(string.ascii_lowercase)
    length = int(request.GET.get('length'), 12)
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
        if request.GET.get('numbers'):
            characters.extend(list(string.digits))
    for _ in range(length):
        the_password += random.choice(characters)
    context = {'password': the_password}
    return render(request, 'generator/password.html', context=context)


def about(request):
    return render(request, 'generator/about.html')
