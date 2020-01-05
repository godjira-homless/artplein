from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'artist', 'title', 'tech', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Item, ItemAdmin)
