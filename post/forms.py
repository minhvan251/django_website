from django import forms
from .models import Post
from django.utils import timezone

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'summary',
            'author',
            'date_posted'
        ]



class RawPostForm(forms.Form):
    title = forms.CharField(label = 'title',max_length = 10)
    summary = forms.CharField(widget=forms.Textarea(
                                attrs = {
                                    'class':'summary-text-area',
                                    'rows': 15,
                                    'cols' : 30
                                }
                                                     )
                            )
    author = forms.CharField()
    date_posted = forms.DateTimeField(initial=timezone.now())
