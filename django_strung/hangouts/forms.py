from django import forms
from .models import Hangout

class HangoutForm(forms.ModelForm):
  class Meta:
    model = Hangout
    fields = ('title', 'members', 'description', 'location', 'date_of_event')