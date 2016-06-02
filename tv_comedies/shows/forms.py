from django import forms

class NewUserForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': False}))
    password = forms.CharField(label='Password', max_length=100)
