from django.urls import path

from . import views

urlpatterns = [
    path('level_register', views.level_register_view, name='level_register'),
]