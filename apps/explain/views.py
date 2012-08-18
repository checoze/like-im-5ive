from django.shortcuts import render
from django.conf import settings
from django.views.generic import DetailView, ListView


def home(request):
    context = {}

    return render(request, 'home/home.html', context)
