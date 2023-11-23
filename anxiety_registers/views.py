from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView

from .models import *
from .forms import *


class AnxietyListView(LoginRequiredMixin, ListView):
    template_name = 'anxiety_list.html'
    queryset = Anxiety.objects.all().order_by('-id')
    login_url = 'landing'


    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class MentalRegisterView(FormView):
    template_name = 'anxiety_register.html'
    form_class = AnxietyForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            anxiety = form.save(commit=False)
            anxiety.user = request.user
            anxiety.save()
            #messages.success(request, 'Registro agregado correctamente')
            return redirect('/mental_health')

        return render(request, self.template_name, {'form': form})
    
class AnxietyDeleteView(LoginRequiredMixin, DeleteView):
    model = Anxiety
    template_name = 'register_confirm_delete.html'  # crea este template
    success_url = reverse_lazy('anxiety_list')
    login_url = 'landing'


"""from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import *
from users.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='landing')
def mental_register_view(request):
    form = AnxietyForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        anxiety = form.save(commit=False)
        anxiety.user = request.user 
        anxiety.save()

        if anxiety:
            messages.success(request, 'Registro agregado correctanente')
            return redirect('home')

    return render(request, 'anxiety_register.html', {
        #Context
        'form': form
    })"""