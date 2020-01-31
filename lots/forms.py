from django import forms
from .models import Lots

from artists.models import Artist


class LotsForm(forms.ModelForm):
    artist_display = forms.CharField(max_length=100)

    class Meta:
        model = Lots
        fields = ('code',
                  'title',
                  'artist_display',
                  'artist',
                  'size',
                  )

    def __init__(self, *args, **kwargs):
        super(LotsForm, self).__init__(*args, **kwargs)
        self.fields['artist_display'].label = "Artist"
        self.fields['artist'].widget = forms.HiddenInput()

    def clean_artist_display(self):
        #artist = self.cleaned_data["artist"]
        artist_display = self.cleaned_data["artist_display"]

        self.cleaned_data["artist"] = "Beke Laci"

        artist = self.cleaned_data["artist"]

        print(artist_display)
        print(artist)

    def clean(self):

        cleaned_data = super().clean()
    # cc_artist_display = cleaned_data["artist_display"]
    # cc_artist = cleaned_data["artist"]

    # cc = cleaned_data
    # print(cc)
