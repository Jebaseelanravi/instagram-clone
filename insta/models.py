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

    def split_biography(self):
        return self.biography.split("\n")


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    posted_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField()
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.caption


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_linked = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    description = models.CharField(max_length=500)
    comment_posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Comment by {} on {}".format(self.user.username, self.post_linked.caption)

    class Meta:
        ordering = ('-comment_posted_on',)


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_linked = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return 'User :{} Liked {} Post '.format(self.user.username,self.post_linked.caption)
