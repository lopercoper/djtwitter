from re import template
from django.shortcuts import render
from django.shortcuts import reverse
from django import forms
from PIL import Image
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse 
from django.shortcuts import redirect
from .forms import (
    SignUpForm,
    CustomUserChangeForm,
)
from .models import (
    UserProfile,
    User
)
from django.views.generic import (
    TemplateView, 
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
    FormView,
    
)

class LandingView(TemplateView):
    template_name = "landing.html"

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse("login")

class EditProfileView(UpdateView):
    form_class = CustomUserChangeForm
    template_name = "edit-profile.html"
            
    def get_queryset(self):
        return User.objects.all()
    
    def get_success_url(self):
        return reverse("postlist")
