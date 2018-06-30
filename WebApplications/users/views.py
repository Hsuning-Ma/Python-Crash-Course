from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request) :
  """Log the user out"""
  logout(request)
  return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request) :
  """Register a new user"""
  if request.method!="POST" :
    #   Display blank registration form
    from = UserCreationForm()
  else :
    #   Process completed form
    from = UserCreationForm(data = request.POST)
    if form.is_valid() :
      new_user = form.save()
      #   Log the user in and then redirect to home page
      authenticated_user = authenticate(
        username = new_user.username, password = request.POST['password1'])
      login(request, authenticated_user)
      return HttpResponseRedirect(reverse('learning_logs:index'))
  context = {'form': form}
  return render(render, 'users/register.html', context)
