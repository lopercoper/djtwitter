
from dataclasses import fields
from django import forms
from PIL import Image
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username','first_name','last_name','description','pfp')
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']
