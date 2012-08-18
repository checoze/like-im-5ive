from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory

from django.utils import simplejson
from django.contrib import messages
from django.http import HttpResponse


from explain.models import Entry, Explanation, Vote
from explain.forms import EntryForm, ExplanationForm, ExplanationFormset, RegistrationForm


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
    context['explanation_form'] = ExplanationForm()
    
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
    
def explanation_submit(request):
    context = {}
    
    if request.method == "POST":
        entry_hex = request.POST.get('entry_hex')
        explanation_form = ExplanationForm(request.POST)
        if explanation_form.is_valid():
            print "is valid"
            explanation_form.save()
    return HttpResponseRedirect(reverse('entry_detail', args=[entry_hex]))

def registration(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Register
            from django.contrib.auth.models import User
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                return redirect("explain.views.home")
            else:
                messages.add_message(request, messages.ERROR, "Use account %s already exists." % username)
                return redirect("explain.views.registartion")

    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, "registration.html", context)


def vote(request, id, type):
    context = {}

    direction = request.POST.get('direction')
    
    if type == 'explanation':
        _object = Explanation.objects.get(id=id)
    elif type == 'comment':
        _object = Explanation.objects.get(id=id)
    else:
        response = simplejson.dumps({ 'success': False })        
        return HttpResponse(response, mimetype='application/json', status=200)

    if direction == 'up':
        value = True
    else:
        value = False
    
    Vote.objects.create(user=request.user, content_object=_object, value=value )
    
    response = simplejson.dumps({ 'success': True })        
    return HttpResponse(response, mimetype='application/json', status=200)

