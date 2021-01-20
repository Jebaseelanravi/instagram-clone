from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Post, Profile


def home(request):
    template = loader.get_template('insta/home.html')

    if request.user.is_anonymous:
        context = {}
        return HttpResponse(template.render(context, request))

    posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    context = {'posts': posts, 'profile': profile}
    return HttpResponse(template.render(context, request))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("user logged in ")
    else:
        return HttpResponse("user ot logged in ")


def signup(request):
    pass
