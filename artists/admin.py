from django.contrib import admin
from .models import Artist

#admin.site.register(Artist)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    ordering = ('name',)
    search_fields = ('name', 'bio')

