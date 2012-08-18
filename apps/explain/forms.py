from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from explain.models import Entry, Explanation

class EntryForm(ModelForm):
    
    class Meta:
        model = Entry
        exclude = ('deleted_date', 'deleted', 'hex', 'slug',)
        
        

class ExplanationForm(ModelForm):
    
    class Meta:
        model = Explanation
        exclude = ('deleted_date', 'deleted', )
        
        

ExplanationFormset = inlineformset_factory(Entry, Explanation, max_num=1, can_delete=False, form=ExplanationForm)