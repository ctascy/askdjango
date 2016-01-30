from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm #, SignupForm2

def signup(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html',{
        'form':form
    })

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request,'accounts/profile.html')
