from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    champion_display = forms.CharField(max_length=100, help_text='type name or username or email')

    class Meta:
        model = Project
        fields = ('title', 'champion_display', 'champion',)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['champion_display'].label = "Add a Champion"
        self.fields['champion'].widget = forms.HiddenInput()
