from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views
app_name = 'book'
urlpatterns = [
    path('', views.book_main_page, name = 'home'),
    path('<int:id>' , views.book_detail, name = 'book-detail' ),
    path('author', views.author_main_page, name = 'main-author'),
    path('author/<int:id>', views.author_detail, name = 'author-detail'),
    path('generic', views.GenericBookView.as_view(),name = 'generic'),
    path('generic/<int:pk>', views.GenericDetailView.as_view(),name = 'generic-detail'),
    path('author/create', views.GenericAuthorCreate.as_view(),name = 'create_author')

]
