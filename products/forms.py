from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title=forms.CharField(label='Product Label', widget=forms.TextInput(attrs={
        "placeholder":"Your Product title"
    }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Your Description",
            "class": "new-class-name",
            "rows": "10",
            "cols": "50"
        }))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # def clean_title(self,*args,**kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not title.endswith("ass"):
    #         raise forms.ValidationError("This is not valid title")
    #     else:
    #         return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='Product Title', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Your Description",
            "class":"new-class-name",
            "rows":"10",
            "cols":"50"
    }))
    price = forms.DecimalField()