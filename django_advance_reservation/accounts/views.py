from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .forms import ApplicationChangeForm
from .forms import myAuthenticationForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation:index')
    else:
        form = ApplicationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/application.html', context)
    
def detail(request, pk):
    application_list = get_user_model()
    form = get_object_or_404(application_list, pk=pk)
    context = {
        'form': form
    }
    return render(request, 'accounts/detail.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect("reservation:index")
    if request.method=="POST":
        form = myAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("reservation:index")
    else:
        form = myAuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect("reservation:index")


def update(request, pk):
    if request.method=="POST":
        form = ApplicationChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('reservation:index')
    else:
        form = ApplicationChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def delete(request):
    request.user.delete()
    return redirect('reservation:index')

