from django.contrib import admin
from django.urls import path
from django.urls import path, include
from post import views as post_views
from .views import register

urlpatterns = [
    path('register/', register, name='register'),

]