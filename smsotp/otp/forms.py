from django import forms


class RegisterNumberForm(forms.Form):
    phone = forms.CharField(max_length=11)

