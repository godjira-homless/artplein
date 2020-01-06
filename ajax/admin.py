from django.contrib import admin
from .models import Ajax


class AjaxAdmin(admin.ModelAdmin):
    list_display = ('code', 'artist', 'title', 'tech',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Ajax, AjaxAdmin)
