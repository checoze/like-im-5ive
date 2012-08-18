from django.shortcuts import render, get_object_or_404
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
    
def entry_detail(request, hex):
    """ Simple homepage invites users to search for or create an entry """
    context = {}
    

    entry = get_object_or_404(Entry, hex=hex)
    context['entry'] = entry
    
    return render(request, 'explain/entry_detail.html', context)