from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from main.models import User
import math

class Comment(models.Model):
    comment_body = models.TextField(max_length=124)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    comment_likes = models.ManyToManyField(User, related_name="comment_likes")
    post_id = models.IntegerField(default=0)
    class Meta:
        ordering = ['-created_date']
    def whenposted(self):
        now = timezone.now()
        diff = now - self.created_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 0: 
                return "Now"
            else:
                return str(seconds) + "s"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "m"
            
            else:
                return str(minutes) + "m"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "h"

            else:
                return str(hours) + "h"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + "d"

            else:
                return str(days) + "d"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + "mo"

            else:
                return str(months) + "mo"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + "y"

            else:
                return str(years) + "y"
class Post(models.Model):
    post_body = models.TextField(max_length=124)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True )
    first_name = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True, related_name='first_name_1')
    created_date = models.DateTimeField(auto_now_add = True)
    is_tweet = models.BooleanField(default=False, blank=True,null=True)
    is_media = models.BooleanField(default=False, blank=True,null=True)
    is_reply = models.BooleanField(default=False, blank=True,null=True)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    liked_post = models.ManyToManyField(User, blank=True, related_name="liked_post")
    def __str__(self):
        return '{}'.format(self.user)
    class Meta:
        ordering = ['-created_date']

    def whenposted(self):
        now = timezone.now()
        diff = now - self.created_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 0: 
                return "Now"
            else:
                return str(seconds) + "s"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "m"
            
            else:
                return str(minutes) + "m"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "h"

            else:
                return str(hours) + "h"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + "d"

            else:
                return str(days) + "d"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + "mo"

            else:
                return str(months) + "mo"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + "y"

            else:
                return str(years) + "y"