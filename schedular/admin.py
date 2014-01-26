from django.contrib import admin
from schedular.models import Event




class EventAdmin(admin.ModelAdmin):
     list_display = ('description', 'schedule','File')

admin.site.register(Event, EventAdmin)
