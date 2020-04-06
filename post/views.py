from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpRequest
from .models import Post
from .forms import PostForm, RawPostForm


# Create your views here.
def Posts(request):
    context = {'posts': Post.objects.all()
               }
    return render(request,'post/post.html',context)
def post_detail(request, id =1 ):
    obj = get_object_or_404(Post, id = id)
    # obj = Post.objects.get(id=id)
    context = {
        'post':obj
    }
    if request.method == 'POST':
        Post.objects.filter(id=id).delete()


    return render(request, 'post/post_detail.html', context)

def create_form(request):
    form = PostForm(request.POST or None)


    if form.is_valid():

        form.save()

    context = {
        'form': form
    }
    return render(request,'post/form.html', context)

def create_raw_form(request):
    form =  RawPostForm()
    if request.method == 'POST':
        form = RawPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            form = RawPostForm()
        else:
            print(form.errors)
    context = {
        'form':form
    }
    return render(request,'post/raw_form.html',context)