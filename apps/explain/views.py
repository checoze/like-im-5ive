from django.shortcuts import render
from django.conf import settings
from django.views.generic import DetailView, ListView

from explain.models import Entry

def home(request):
    """ Simple homepage invites users to search for or create an entry """
    context = {}
    
    if request.method == "POST":
        term = request.POST.get('search')
        print term
    
    
        entry = Entry.objects.get_until_create()
        entry.name = term
        entry.save()
    else:
        pass
    
    return render(request, 'explain/home.html', context)