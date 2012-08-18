from django.shortcuts import render
from django.conf import settings

def home(request):
    context = {}

    return render(request, 'home/home.html', context)
