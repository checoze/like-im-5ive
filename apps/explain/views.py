from django.shortcuts import render
from django.conf import settings
from django.views.generic import DetailView, ListView

from explain.models import Entry

def home(request):
    """ Simple homepage invites users to search for or create an entry """
    context = {}
    print request.POST
    
    #term, created = Entry.objects.get_or_create()
    

    return render(request, 'explain/home.html', context)
