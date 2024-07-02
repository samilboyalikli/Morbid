from django import forms


class VeriForm(forms.Form):
    kilo = forms.FloatField(label='Kilo')
    boy = forms.FloatField(label='Boy')
