from django import forms
from django.forms.models import inlineformset_factory

from explain.models import Entry, Explanation

BASE_EXCLUDE_FIELDS = ('deleted_date','deleted',)

class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        exclude = BASE_EXCLUDE_FIELDS
        exclude += ('hex', 'slug',)
        

class ExplanationForm(forms.ModelForm):
    
    class Meta:
        model = Explanation
        exclude = BASE_EXCLUDE_FIELDS


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Explanation
        exclude = BASE_EXCLUDE_FIELDS


class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


ExplanationFormset = inlineformset_factory(Entry, Explanation, max_num=1, can_delete=False, form=ExplanationForm)