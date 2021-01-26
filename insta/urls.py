from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home,name="home"),
    path('user/<str:username>', views.user_profile,name="user_profile"),
    path('add_comment', views.add_comment,name="add_comment")
]
