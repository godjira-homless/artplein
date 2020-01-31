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
