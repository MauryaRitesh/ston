from django import forms
from .models import Startup, Investor


class StartupForm(forms.ModelForm):

    class Meta:
        model = Startup
        fields = ('name','url', 'address', 'domain', 'subdomain')


class InvestorForm(forms.ModelForm):

    class Meta:
        model = Investor
        fields = ('name', 'age', 'net_worth',)
