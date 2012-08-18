from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from explain.models import Entry
from explain.forms import EntryForm

def home(request):
    """ Simple homepage invites users to search for or create an entry """
    context = {}
    
    if request.method == "POST":
        term = request.POST.get('search')    
    
        try:
            entry = Entry.objects.get(name=term)
        except:
            return entry_prompt(request)
            #return HttpResponseRedirect(reverse('entry_prompt'))
    
        #entry = Entry.objects.get_until_create()
        #entry.name = term
        #entry.save()
    else:
        return render(request, 'explain/home.html', context)
    
def entry_detail(request, hex):
    """ Simple homepage invites users to search for or create an entry """
    context = {}
    

    entry = get_object_or_404(Entry, hex=hex)
    context['entry'] = entry
    
    return render(request, 'explain/entry_detail.html', context)
    
    
def entry_prompt(request):
    context = {}

    if request.user.is_authenticated():
        context['current_user'] = request.user
    else:
        context['current_user'] = "garrett"
        
    context['term'] = request.POST.get('search')
    context['entry_form'] = EntryForm()
    
    return render(request, 'explain/entry_prompt.html', context)