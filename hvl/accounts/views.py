from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm 


# Create your views here.

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name= "registration/register.html"
