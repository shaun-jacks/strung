from django.shortcuts import render

from .forms import HangoutForm
from .models import Hangout
from django.contrib import messages

def create_hangout(request):

  if request.method == 'POST':
    form = HangoutForm(request.POST)
    if form.is_valid():
      hangout = form.save(commit=False)
      hangout.author = request.user
      hangout.save()
      messages.success(request, 'hangout created!')

      return render(request, 'hangouts/create_hangout.html', {'form':form})

  else:
    form = HangoutForm()
  
  context = {
    'form': form,
  }
  return render(request, 'hangouts/create_hangout.html', context)