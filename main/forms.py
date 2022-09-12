from dataclasses import fields
from django import forms
from PIL import Image
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import Photo
User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)
    
    class Meta:
        model =  User
        fields = ( 'first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username','first_name','last_name','pfp')
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']
