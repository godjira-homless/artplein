from django import forms
from django.http import request

from .models import Tetelek

from artists.models import Artist


class TetelekForm(forms.ModelForm):
    artist = forms.CharField(max_length=100, required=False)
    # photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Tetelek
        fields = (
            'code',
            'title',
            'artist',
            'photo',
                  )

    def clean_artist(self, commit=True):
        artist = self.cleaned_data.get("artist")
        artist, created = Artist.objects.get_or_create(name=artist)
        self.cleaned_data['artist'] = artist
        return artist

    def __init__(self, *args, **kwargs):
        super(TetelekForm, self).__init__(*args, **kwargs)
