from django import forms
from django.forms import TextInput

from .models import Item



class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['code',
                  'title',
                  'description',
                  'size',
                  'tech',
                  'artist'
                  ]

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['artist'].widget = forms.TextInput(attrs={
            'id': 'contact_name_search_input'})

