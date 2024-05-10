from django import forms
from .models import FinancialOrganization


class FinancialOrganizationForm(forms.ModelForm):
    class Meta:
        model = FinancialOrganization
        fields = ['name', 'address', 'phone_number', 'email', 'is_active']
