from django.shortcuts import render

from .forms import HangoutForm
from .models import Hangout
from django.contrib import messages

def create_hangout(request):

  if request.method == 'POST':
    form = HangoutForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'hangout created!')

      return

  else:
    form = HangoutForm()
  
  context = {
    'form': form,
  }
  return render(request, 'hangouts/create_hangout.html', context)