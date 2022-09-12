from dataclasses import field, fields
from django import forms
from posts.models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'post_body',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment_body',
        )

        