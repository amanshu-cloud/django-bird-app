from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'age', 'name', 'gender', 'country', 'email', 'password')  

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'name', 'gender', 'country', 'email', 'password')  

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
