from django import forms

class NewUserForm(forms.Form):
    user_name = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
