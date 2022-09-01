from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
User = get_user_model()

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=254, required=True)
    username = forms.CharField(max_length=20, required=True)
    class Meta:
        model =  User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username','email')
        
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']
    