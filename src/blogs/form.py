from django import forms
from .models import Blogs

class BlogsModelForm(forms.ModelForm):
    post = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "write your thought",
                "class": "new-class-name",
                "id": "product-id-for-textarea",
                'rows': 10,
                'cols': 20
            }
        )
    )
    class Meta:
        model=Blogs
        fields = [
            'topic',
            'post',
            'online'
        ]