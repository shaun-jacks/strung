from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
  return render(request,
    'users/profile.html',
    {'section': 'profile'})


def register(request):
  form = UserCreationForm()
  return render(request, 'users/register.html', {'form': form})

def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request,
                          username=cd['username'],
                          password=cd['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponse('Authenticated successfully')
        else:
          return HttpResponse('Disabled account')
      else:
        return HttpResponse('Invalid login')
  else:
    form = LoginForm()
  return render(request, 'users/login.html', {'form': form})

def logout(request):

  return render(request, 'users/logout.html')


def signup(request):

  return render(request, 'users/signup.html')


