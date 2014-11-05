from django import forms

class DatabaseForm(forms.Form):
    id = forms.CharField()
    name = forms.CharField()
    engine = forms.CharField()
    host = forms.CharField()
    port = forms.IntegerField()
    user = forms.CharField()
    password = forms.CharField()
