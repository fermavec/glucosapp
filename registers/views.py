from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import *
from users.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='landing')
def level_register_view(request):
    
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        reading = form.save(commit=False)
        reading.user = request.user 
        reading.save()

        if reading:
            messages.success(request, 'Registro agregado correctanente')
            return redirect('/readings/')

    return render(request, 'level_register.html', {
        #Context
        'form': form
    })