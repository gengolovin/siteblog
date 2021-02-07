from django import forms
from captcha.fields import CaptchaField
from .models import Comment
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserCommentForm(forms.ModelForm):
        
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки',
              error_messages={'invalid': 'Неправильный текст'})
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'captcha')