from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


class ReadingListView(LoginRequiredMixin, ListView):
    template_name = 'readings/list_readings.html'
    queryset = Reading.objects.all().order_by('-id')
    login_url = 'landing'


    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ReadingDetailView(LoginRequiredMixin, DetailView):
    model = Reading
    template_name = 'readings/reading.html'
    login_url = 'landing'

class ReadingSearchListView(LoginRequiredMixin, ListView):
    template_name = 'readings/search.html'
    login_url = 'landing'

    def get_queryset(self):
        query = self.query()
        query = query.lower()

        if query == 'glucose':
            r_query = 1
        elif query == 'carbohidrates':
            r_query = 2
        elif query == 'insuline-basal':
            r_query = 3
        elif query == 'insuline-bolus':
            r_query = 4
        elif query == 'exercise':
            r_query = 5
        elif query == 'medication':
            r_query = 6
        else:
            r_query = None

        return Reading.objects.filter(category=r_query)
    
    
    def query(self):
        return self.request.GET.get('q')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['reading_list'].count()

        return context


class ReadingDeleteView(LoginRequiredMixin, DeleteView):
    model = Reading
    template_name = 'readings/reading_confirm_delete.html'  # crea este template
    success_url = reverse_lazy('list_readings')
    login_url = 'landing'
