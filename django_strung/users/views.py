from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.forms import modelformset_factory
from .models import Instrument, Profile
from .forms import LoginForm, UserRegistrationForm, \
  UserEditForm, ProfileEditForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      # Create a new user object but avoid saving yet
      new_user = user_form.save(commit=False)
      # Set the chosen password
      new_user.set_password(
        user_form.cleaned_data['password']
      )
      # Save the user object
      new_user.save()
      return render(request, 'users/register_done.html',
       {'new_user' : new_user})
  else:
    user_form = UserRegistrationForm()
  return render(request, 'users/register.html',
             {'user_form': user_form})


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

@login_required
def edit(request):
  if request.method == 'POST':
    user_form = UserEditForm(instance=request.user, \
      data=request.POST,
      files=request.FILES)
    profile_form = ProfileEditForm(instance=request.user.profile, \
      data=request.POST,
      files=request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile = profile_form.save(commit=False)
      profile.user = request.user
      profile.save()
    else:
      return HttpResponse('Form Invalid')
  else:
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
  return render(request, 'users/edit_profile.html', {'user_form' : user_form,
  'profile_form': profile_form})
  
