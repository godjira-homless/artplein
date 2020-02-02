from django import forms
from django.http import request

from .models import Tetelek

from artists.models import Artist


class TetelekForm(forms.ModelForm):
    # artist_display = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Tetelek
        fields = ('title',
                  'artist',
                  )


    def clean_artist(self, commit=True):
        artist = self.cleaned_data.get("artist")
        artist, created = Artist.objects.get_or_create(name=artist)
        self.cleaned_data['artist'] = artist
        return artist

    def __init__(self, *args, **kwargs):
        super(TetelekForm, self).__init__(*args, **kwargs)
