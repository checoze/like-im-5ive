from django.shortcuts import render
from django.conf import settings
from django.views.generic import DetailView, ListView


def home(request):
    """ Simple homepage invites users to search for or create an entry """
    context = {}

    return render(request, 'explain/home.html', context)
