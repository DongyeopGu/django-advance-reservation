from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import User
# Create your views here.

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:application')
    else:
        form = ApplicationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/application.html', context)
def update(request, pk):
    pass

def delete(request, pk):
    pass

def detail(request, pk):
    pass
