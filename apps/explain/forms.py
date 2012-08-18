from django.forms import ModelForm
from explain.models import Entry

class EntryForm(ModelForm):
    
    class Meta:
        model = Entry
        exclude = ('deleted_date', 'deleted', 'hex', 'slug',)