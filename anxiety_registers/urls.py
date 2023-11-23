from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnxietyListView.as_view(), name='anxiety_list'),
    path('anxiety_register', views.MentalRegisterView.as_view(), name='anxiety_register'),
    path('<int:pk>/delete/', views.AnxietyDeleteView.as_view(), name='register_delete'),
]