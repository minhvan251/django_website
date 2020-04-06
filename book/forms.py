from django import forms
from .models import Book, Author
from django.utils import timezone

class CreateAuthor(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

