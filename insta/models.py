
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    posted_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.caption


