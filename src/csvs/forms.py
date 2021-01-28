from django import forms
from .models import Csvs


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csvs
        fields = ('file_name',)