from django import forms
from .models import Users
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = Users
        fields = [
                    'username',
                    'email',
                    'password1',
                    'password2'
        ]
