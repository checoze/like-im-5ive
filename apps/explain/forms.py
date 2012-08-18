from django import forms
from django.forms.models import inlineformset_factory

from explain.models import Entry, Explanation

class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        exclude = ('deleted_date', 'deleted', 'hex', 'slug',)
        
        

class ExplanationForm(forms.ModelForm):
    
    class Meta:
        model = Explanation
        exclude = ('deleted_date', 'deleted', )
        
class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordField()

ExplanationFormset = inlineformset_factory(Entry, Explanation, max_num=1, can_delete=False, form=ExplanationForm)