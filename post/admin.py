from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'visit_date')
