from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField()
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    description = models.TextField (max_length= 200)
    followers = models.ManyToManyField("self", blank=True, symmetrical=False)
    following = models.ManyToManyField("self", blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)

class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'