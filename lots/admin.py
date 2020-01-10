from django.contrib import admin
from .models import Lots


class LotAdmin(admin.ModelAdmin):
    list_display = ('code', 'title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Lots, LotAdmin)
