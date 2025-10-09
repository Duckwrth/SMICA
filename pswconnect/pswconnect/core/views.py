from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    if request.user.role == 'client':
        return render(request, 'client/dashboard.html')
    else:
        return render(request, 'psw/dashboard.html')
