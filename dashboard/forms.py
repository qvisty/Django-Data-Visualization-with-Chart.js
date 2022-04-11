from django import forms
from .models import CountryData, Freetime


class CountryDataForm(forms.ModelForm):
    class Meta:
        model = CountryData
        fields = "__all__"


class FreetimeForm(forms.ModelForm):
    class Meta:
        model = Freetime
        fields = "__all__"
