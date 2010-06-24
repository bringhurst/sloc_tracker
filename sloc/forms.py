from django import forms
from models import Segment, Language, SlocType
from datetime import date

class SlocForm(forms.Form):
    sloc = forms.IntegerField(required=True)
    segment = forms.ModelChoiceField(Segment.objects.all(),required=True)
    language = forms.ModelChoiceField(Language.objects.all(),required=True)
    generated_date = forms.DateField(initial=date.today(),required=True)
    reported_by = forms.CharField(max_length=100,required=True)
    sloc_type = forms.ModelChoiceField(SlocType.objects.all(),required=True)
