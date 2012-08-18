from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory


from explain.models import Entry, Explanation
from explain.forms import EntryForm, ExplanationForm, ExplanationFormset

def home(request):
    """ Simple homepage invites users to search for or create an entry """
    context = {}
    
    if request.method == "POST":
        term = request.POST.get('search')    
    
        try:
            entry = Entry.objects.get(name=term)
        except:
            return entry_prompt(request)

    else:
        return render(request, 'explain/home.html', context)

    
def entry_detail(request, hex):
    """ Entry Detail """
    context = {}
    
    entry = get_object_or_404(Entry, hex=hex)
    context['entry'] = entry
    
    return render(request, 'explain/entry_detail.html', context)
    
    
def entry_prompt(request):
        
    context = {}
    
    if request.user.is_authenticated():
        context['current_user'] = request.user.id
    else:
        context['current_user'] = "garrett"
    
    context['term'] = request.POST.get('search')
    initial_data = {'name': request.POST.get('search') }
    context['entry_form'] = EntryForm(initial_data)
    context['formset'] = ExplanationFormset()
    
    
    return render(request, 'explain/entry_prompt.html', context)
    
def entry_submit(request):
    context = {}

    if request.method == "POST":

        entry_form = EntryForm(request.POST)
        
        if entry_form.is_valid():

            print "is valid"
            entry = entry_form.save(commit=False)
            formset = ExplanationFormset(request.POST, instance=entry)
            if formset.is_valid():
                entry_form.save()
                formset.save()
            
            return HttpResponseRedirect(reverse('entry_detail', args=[entry.hex]))
            
            
    return render(request, 'explain/entry_detail.html', context)