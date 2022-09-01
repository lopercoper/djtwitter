from tkinter import CASCADE
from django.db import models

from main.models import User

class Post(models.Model):
    post_body = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True )
    created_date = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-created_date']