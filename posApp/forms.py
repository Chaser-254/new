from django import forms

from posApp.models import Creditor, Debtors, Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = ['name','amount_owed','date_owed']

class CreditorForm(forms.ModelForm):
    class Meta:
        model = Creditor
        fields = ['name','amount','due_date']