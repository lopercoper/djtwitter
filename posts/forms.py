from dataclasses import field
from django import forms
from posts.models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'post_body',
        )