from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Post, Profile, Comment, Like
from .forms import PostForm, ProfileForm
from django.contrib.auth.models import User


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
    # posts = Post.objects.all()
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
        post.likes -= 1
    except Like.DoesNotExist:

        Like.objects.create(post_linked=post, user=request.user)
        post.likes += 1
    post.save()
    return redirect(reverse('home'))


def add_post(request):
    template = loader.get_template('insta/post.html')
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = profile
            fs.save()
            return redirect(reverse('home'))
    else:
        form = PostForm()
        pass

    context = {'form': form ,'profile':profile}
    return HttpResponse(template.render(context, request))


def edit_profile(request, username):
    template = loader.get_template('insta/edit_profile.html')
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            profile.biography = form.cleaned_data['biography']
            profile.profile_pic = form.cleaned_data['profile_pic']
            profile.phone_number = form.cleaned_data['phone_number']
            profile.save()
            return redirect(reverse('home'))
    else:

        form = ProfileForm(initial={'username': username,
                                    'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'phone_number': profile.phone_number,
                                    # 'profile_pic': profile.profile_pic.url,
                                    'biography': profile.biography})

    context = {'form': form, 'user': user, 'profile':profile}
    return HttpResponse(template.render(context, request))
