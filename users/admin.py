from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Patient)
admin.site.register(PatientProfile)