from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request,'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')

def dashboard(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'dashboard/index.html')
    else:
        return render(request,'account/login.html')