from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=20)
    country = forms.CharField(max_length=50)