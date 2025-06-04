from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, HraForm
from .models import Hra_v_Robloxe

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def hry_list_view(request):
    hry = Hra_v_Robloxe.objects.all().order_by('-hlasy')  # '-' for descending order
    return render(request, 'hry_list.html', {'hry': hry})

@login_required
def pridat_hru_view(request):
    if request.method == 'POST':
        form = HraForm(request.POST, request.FILES)
        if form.is_valid():
            hra = form.save(commit=False)
            hra.hlasy = '0'  # Initialize votes to 0
            hra.save()
            return redirect('hry_list')
    else:
        form = HraForm()
    return render(request, 'pridat_hru.html', {'form': form})
