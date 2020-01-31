from django import forms
from .models import Tetelek

from artists.models import Artist


class TetelekForm(forms.ModelForm):
    # artist_display = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)

    class Meta:
        model = Tetelek
        fields = ('title',
                  'artist',
                  )

    def clean_artist(self, commit=True):
        artist = self.cleaned_data.get("artist")
        if not artist:
            raise forms.ValidationError("Artist is a required field.")
        else:
            artist, created = Artist.objects.get_or_create(name=artist)
            self.cleaned_data['artist'] = artist
            return artist

    def __init__(self, *args, **kwargs):
        super(TetelekForm, self).__init__(*args, **kwargs)
        # self.fields['artist_display'].label = "Artist"
        # self.fields['artist'].widget = forms.HiddenInput()
