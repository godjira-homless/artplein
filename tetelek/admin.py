from django.contrib import admin

from .models import Tetelek


class TetelekAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tetelek, TetelekAdmin)
