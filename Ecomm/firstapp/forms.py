from django import forms
from .models import Orders
class customerform(forms.Form):
    name = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)

class orderform(forms.ModelForm):
    class Meta:
        model=Orders
        fields ='__all__'

