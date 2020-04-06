from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpRequest
from .models import Book, Author
from .forms import CreateAuthor
from django.views.generic import (

    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# from .forms import PostForm, RawPostForm
# Create your views here.

class GenericBookView(ListView):
    # model = Book
    template_name = 'book/generic_book.html'
    queryset = Book.objects.all()
    paginate_by = 2
class GenericDetailView(DetailView):
    template_name = 'book/generic_book_detail.html'
    queryset = Book.objects.all()

    # def get_object(self, queryset=None):
    #     id = self.kwargs.get('id')
    #     return

class GenericAuthorCreate(CreateView):
    model = Author
    queryset = Author.objects.all()
    form_class = CreateAuthor
    template_name = 'author/author_form.html'




def book_main_page(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors
    }
    return render(request,'book/book_main_page.html',context)

def book_detail(request,id ):
    book = Book.objects.get(id = id)
    context = {
        'book': book
    }
    return render(request, 'book/book_detail.html', context)
def author_main_page(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books
    }
    return render(request,'author/author_main_page.html',context)
def author_detail(request,id ):

    author = Author.objects.get(id = id)
    book = list(Book.objects.filter(author=author))
    context = {
        'author': author,
        'book' : book

    }
    return render(request, 'author/author_detail.html', context)