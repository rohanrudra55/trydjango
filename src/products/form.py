from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label='Item',
        widget=forms.TextInput(
            attrs={
                "placeholder": "product name"
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "describe product",
                "class": "new-class-name",
                "id": "product-id-for-textarea",
                'rows': 10,
                'cols': 20
            }
        )
    )
    price     = forms.DecimalField(required=True, initial=99.00)
    avability = forms.BooleanField(required=True,initial=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'avability'
        ]