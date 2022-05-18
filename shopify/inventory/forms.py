from django import forms

class NewItemForm(forms.Form):
    name = forms.CharField(label='Product Name', max_length=50)
    price = forms.IntegerField(label='Price')