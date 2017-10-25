from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from imagekit.forms import ProcessedImageField

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(UserCreateForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

