from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'cell_number']


class ClientPlanForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'cell_number', 'plan', 'start_date']

        # def __init__(self, *args, **kwargs):
        #     super(ClientPlanForm, self).__init__(*args, **kwargs)
        #     self.fields['start_date'].widget.attrs.update({
        #         'id': 'id_start_date'})