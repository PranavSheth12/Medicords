from django.shortcuts import render,redirect
from .models import Contact, Patientinfo
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()

        messages.success(request, 'Your message has been sent.')
        return redirect('home')
    return render(request,'contactus.html')

def profile(request):
    return render(request,'profile.html')

def patientinfo(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        report = request.POST.get('report')
        
        info = Patientinfo(firstname=firstname,lastname=lastname,username=username,email=email,phone=phone,gender=gender,report=report)
        info.save()

        messages.success(request, 'Your have registered successfully.')
        return redirect('home')
    return render(request,'patientinfo.html')