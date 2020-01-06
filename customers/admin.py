from django.contrib import admin
from .models import Person

# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name')
