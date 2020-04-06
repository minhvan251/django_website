from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):

    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=150)
    author = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default =timezone.now)
    def get_absolute_url(self):
        return reverse('post:post-detail',kwargs={'id': self.id})

# Create your models here.
