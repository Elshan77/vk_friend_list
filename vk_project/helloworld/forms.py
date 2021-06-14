from django import forms

class NameForm(forms.Form):
    user_id = forms.CharField(label='user id', max_length=100)
    token = forms.CharField(label='token', max_length=300)