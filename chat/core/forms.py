from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=80, required=True)
    last_name = forms.CharField(max_length=80, required=False)
    email = forms.EmailField(max_length=254)
    class meta:
        model = User
        field = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ["message","receiver","sender","replyStatus"]