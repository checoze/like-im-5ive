from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.contrib.contenttypes.models import ContentType

from django.utils import simplejson
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse


from explain.models import Entry, Explanation, Vote
from explain.forms import EntryForm, ExplanationForm, ExplanationFormset, RegistrationForm


def home(request):
    """ Simple homepage invites users to search for or create an entry """
    context = {}
    
    if request.method == "POST":
        term = request.POST.get('search')
        context['search'] = term

        try:
            entry = Entry.objects.get(name=term)
            return redirect(reverse('entry_detail', args=[entry.hex]))

        except Entry.DoesNotExist:
            # Try to find similar ones
            from django.db.models.query import Q
            entries = Entry.objects.filter(Q(name__istartswith=term) | Q(name__iendswith=term))
            if not entries.exists():
                request.method = "GET"
                return entry_prompt(request, term)

            context['entries'] = entries
            return render(request, "explain/search_results.html", context)

    else:
        return render(request, 'explain/home.html', context)

    
def entry_detail(request, hex):
    """ Entry Detail """
    context = {}
    
    entry = get_object_or_404(Entry, hex=hex)
    context['entry'] = entry
    context['explanation_form'] = ExplanationForm()
    
    return render(request, 'explain/entry_detail.html', context)
    
    
def entry_prompt(request, search_term=None):
    context = {}
    if request.method == "POST":
        entry_form = EntryForm(request.POST)
        print("validate")
        print(entry_form.errors)
        if entry_form.is_valid():
            print('step 1')
            entry = entry_form.save(commit=False)
            formset = ExplanationFormset(request.POST, instance=entry)
            if formset.is_valid():
                print("save")
                entry_form.save()
                formset.save()
                return HttpResponseRedirect(reverse('entry_detail', args=[entry.hex]))
    else:
        if request.user.is_authenticated():
            context['current_user'] = request.user.id
        else:
            context['current_user'] = User.objects.get(username="anon").id

        context['term'] = search_term
        initial_data = {'name': search_term }
        entry_form = EntryForm(initial_data)
        formset = ExplanationFormset()
    context['entry_form'] = entry_form
    context['formset'] = formset

    return render(request, 'explain/entry_prompt.html', context)

    
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
                user.save()
                from django.contrib.auth import authenticate, login
                user = authenticate(username=username, password=password)
                if user.is_active:
                    login(request, user)
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

    #What type of object
    if type == 'explanation':
        _object = Explanation.objects.get(id=id)
    elif type == 'comment':
        _object = Explanation.objects.get(id=id)
    else:
        response = simplejson.dumps({ 'success': False })
        return HttpResponse(response, mimetype='application/json', status=200)


    #Only Vote once
    explanation_type = ContentType.objects.get(app_label="explain", model="explanation")
    vote, created = Vote.objects.get_or_create(user=request.user, content_type=explanation_type, object_pk=_object.id)

    #Save value of vote
    if created:
        if direction == 'up':
            value = True
        else:
            value = False
        vote.value = value
        vote.save()
        
        response = simplejson.dumps({ 'success': True, 'value': _object.score })
        return HttpResponse(response, mimetype='application/json', status=200)
    else:
        response = simplejson.dumps({ 'success': False, 'message':"Already voted" })
        return HttpResponse(response, mimetype='application/json', status=200)