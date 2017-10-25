from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import UserCreateForm
from imagekit.forms import ProcessedImageField

from . models import IGPost, Comment, Like
from accounts.models import UserProfile


class PostPictureForm(ModelForm):
    class Meta:
        model = IGPost
        fields = ['title', 'image']


class ProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'description']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
