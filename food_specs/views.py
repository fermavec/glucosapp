from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


class FoodListView(LoginRequiredMixin, ListView):
    template_name = 'food_specs/list_food.html'
    queryset = FoodInformation.objects.all().order_by('clasification')
    login_url = 'landing'


    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class FoodSearchListView(LoginRequiredMixin, ListView):
    template_name = 'food_specs/search.html'
    login_url = 'landing'

    def get_queryset(self):
        query = self.query()
        query = query.capitalize()

        
        return FoodInformation.objects.filter(food=query)
    
    
    def query(self):
        return self.request.GET.get('q')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['object_list'].count()


        return context