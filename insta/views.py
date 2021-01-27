from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Post, Profile, Comment, Like
import json


def home(request):
    template = loader.get_template('insta/home.html')

    if request.user.is_anonymous:
        context = {}
        return HttpResponse(template.render(context, request))

    posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    comments = Comment.objects.all()
    context = {'posts': posts, 'profile': profile, 'comments': comments}
    return HttpResponse(template.render(context, request))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("user logged in ")
    else:
        return HttpResponse("user ot logged in ")


def signup(request):
    pass


def user_profile(request, username):
    template = loader.get_template('insta/profile.html')
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author__user__username=request.user.username)
    posts = Post.objects.all()
    context = {'profile': profile, 'posts': posts}
    return HttpResponse(template.render(context, request))


def add_comment(request):
    if request.POST:
        description, id = request.POST['description'], request.POST['demo']
        post = Post.objects.get(pk=id)
        if description is not None:
            Comment.objects.create(post_linked=post, description=description, user=request.user)
            return redirect(reverse('home'))


def like_post(request, postid):
    post = Post.objects.get(id=postid)
    try:
        is_Liked = Like.objects.get(post_linked=post, user__username=request.user.username)
        Like.objects.filter(post_linked=post, user__username=request.user.username).delete()
        post.likes -=1
    except Like.DoesNotExist:

        Like.objects.create(post_linked=post, user=request.user)
        post.likes +=1
    post.save()
    return redirect(reverse('home'))
