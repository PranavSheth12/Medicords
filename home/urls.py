from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contactus',views.contactus,name='contactus'),
    path('profile',views.profile,name='profile'),
    path('patientinfo',views.patientinfo,name='patientinfo'),
]