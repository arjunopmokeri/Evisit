from django import forms

class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()
    seller = forms.CharField()
    category = forms.CharField()