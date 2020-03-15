from django import forms
from account.models import customerinfo

class customerform(forms.ModelForm):
    class Meta():
        model = customerinfo
        fields = '__all__'
