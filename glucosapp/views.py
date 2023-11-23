# Django Framework Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.contrib.auth.decorators import login_required

#Forms
from .forms import RegisterForm

# Models
from readings.models import Reading
from anxiety_registers.models import Anxiety


@login_required(login_url='landing')
def index(request):
    readings = Reading.objects.all().order_by('-id')
    anxiety_regs = Anxiety.objects.all().order_by('-id')

    return render(request, 'index.html', {
        #context
        'title': 'Registros | Glucosapp',
        'message': 'Agrega un registro',
        'readings': readings,
        'anxiety_regs': anxiety_regs
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.username}!')
            return redirect('home')
        else:
            messages.error(request,'Error de usuario o contraseña')

    return render(request, 'users/login.html', {
        # Context
    })


def logout_view(request):
    logout(request)
    return redirect('landing')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('home')

    return render(request, 'users/register.html', {
        #Context
        'form': form
    })


def landing(request):
    return render(request, 'landing.html', {
        #Context
    })