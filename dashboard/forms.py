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


from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

from .models import Employee


class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["days", "firstName", "department"]
