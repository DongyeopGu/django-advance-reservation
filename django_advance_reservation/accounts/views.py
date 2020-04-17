from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm, ApplicationChangeForm
from .models import User
from django.contrib.auth import get_user_model
# Create your views here.

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail')
    else:
        form = ApplicationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/application.html', context)
    
def update(request, pk):
    if request.method=="POST":
        form = ApplicationChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:application')
    else:
        form = ApplicationChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def delete(request):
    request.user.delete()
    return redirect('accounts/application')


def detail(request, pk):
    application_list = get_user_model()
    user = get_object_or_404(application_list, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

