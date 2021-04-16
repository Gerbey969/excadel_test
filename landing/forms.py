from django import forms

class ProductSearchForm(forms.Form):
    itemName = forms.CharField()