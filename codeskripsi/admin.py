from django.contrib import admin
from .models import Presence, Class

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'timestamp', 'schedule', 'schedule_limit',  'class_name',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name',)