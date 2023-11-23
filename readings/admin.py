from django.contrib import admin

from .models import *

class ReadingAdmin(admin.ModelAdmin):
    fields = ('user', 'reading_value', 'category', 'notes')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Reading, ReadingAdmin)
#admin.site.register(Category)
