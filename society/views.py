from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, 'society/home.html')

def welcome(request):
    return render(request, 'society/welcome.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'society/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'society/loginuser.html',{ 'form':AuthenticationForm(), 'output':'Username or Password did not matched'})
        else:
            login(request, user)
            return  redirect('home')
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('welcome')

