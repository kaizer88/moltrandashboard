from django import forms
from .models import Town, Property, Tenant, Agent


class TownForm(forms.ModelForm):
    class Meta:
        model = Town
        fields = ['name', 'code', 'province']

class UploadForm(forms.Form):
    upload = forms.FileField(required=True, label="Upload")