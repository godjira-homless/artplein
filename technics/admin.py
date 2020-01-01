from django.contrib import admin
from .models import Technic

class TechnicAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Technic, TechnicAdmin)
