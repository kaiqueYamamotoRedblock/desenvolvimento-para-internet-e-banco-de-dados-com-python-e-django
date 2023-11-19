from django.contrib import admin

from core.models import Evento

class EventosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_evento', 'data_criacao']

# Register your models here.
admin.site.register(Evento, EventosAdmin)