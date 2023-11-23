from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReadingListView.as_view(), name='list_readings'),
    path('search/', views.ReadingSearchListView.as_view(), name='search'),
    path('<slug:slug>/', views.ReadingDetailView.as_view(), name='reading_detail'),
    path('<int:pk>/delete/', views.ReadingDeleteView.as_view(), name='reading_delete'),
]
