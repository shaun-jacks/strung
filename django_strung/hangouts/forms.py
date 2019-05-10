from django import forms
from .models import Hangout

class HangoutForm(forms.ModelForm):
  class Meta:
    model = Hangout
    fields = ('members', 'description', 'location', 'date_of_event')