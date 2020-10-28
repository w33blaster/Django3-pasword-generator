from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    characters = list('abcdefghijklmniopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+?><.'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    Length = int(request.GET.get('Length', 12))

    thepasswprd = ''

    for x in range(Length):
        thepasswprd += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepasswprd})
