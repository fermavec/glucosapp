from django.contrib import admin
from django.urls import path, include


from . import views
from readings.views import *
from registers.views import *
from anxiety_registers.views import *
from food_specs.views import *


urlpatterns = [
    #path('', ReadingListView.as_view(), name='home'),
    path('', views.index, name='home'),
    path('users/login', views.login_view, name='login'),
    path('users/logout', views.logout_view, name='logout'),
    path('users/register', views.register_view, name='register'),
    path('admin/', admin.site.urls),
    path('glucosapp/', views.landing, name='landing'),
    path('readings/', include('readings.urls')),
    path('registers/', include('registers.urls')),
    path('mental_health/', include('anxiety_registers.urls')),
    path('food_specs/', include('food_specs.urls')),
]
