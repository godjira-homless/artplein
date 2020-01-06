from django.contrib import admin
from .models import Technic

class TechnicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Technic, TechnicAdmin)
