from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.
def register(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'accout created')
            return redirect('book:home')
    else:
        form = CustomUserCreationForm()


    return render(request,'users/register.html',{'form': form})