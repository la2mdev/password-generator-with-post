from django import forms
from . import utils


class PasswordGenerator(forms.Form):
    length = forms.IntegerField(label='length', min_value=7, max_value=21, initial=10,
                                required=True, widget=forms.TextInput(attrs={'type': 'range', 'min': 7, 'max': 21}))
    has_numbers = forms.BooleanField(label='numbers', required=False)
    has_uppercases = forms.BooleanField(label='uppercases', required=False)
    has_special = forms.BooleanField(
        label='special characters', required=False)

    def clean_length(self, *args, **kwargs):
        length = self.cleaned_data.get('length')
        return int(length)

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        password = utils.generate_password(data)
        return password
