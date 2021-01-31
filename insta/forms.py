from django import forms
from django.forms import ModelForm

from .models import Post, Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'location', 'caption']


class ProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    profile_pic = forms.ImageField(required=False)
    username = forms.CharField(max_length=500,required=True)
    first_name = forms.CharField(max_length=500, required=False)
    last_name = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    biography = forms.CharField(required=False, widget=forms.Textarea())


