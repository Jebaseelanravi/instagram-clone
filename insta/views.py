from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


def home(request):
    template = loader.get_template('insta/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login_user(request):

    username = request.POST['username']
    password = request.POST['password']
    print (username)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("user logged in ")
    else:
        return HttpResponse("user ot logged in ")

def signup(request):
    pass