from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField()
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)