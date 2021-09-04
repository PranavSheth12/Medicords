from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            #messages.error(request, 'Wrong username or password')
            return render(request,'login.html',)
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email,
                                            password=f'{password}')
        user.save()
        messages.success(request,"You have signed up successfully")
        return redirect('login')
    return render(request,'signup.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')