from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    caption = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    posted_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField()

    def __str__(self):
        return self.caption