from django import forms
from django.forms import TextInput, PasswordInput

custom_field = "appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mt-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=TextInput(attrs={"class": f"{custom_field}", "value": "admin"}))
    password = forms.CharField(max_length=63, widget=PasswordInput(attrs={"class": f"{custom_field}", "value": "admin"}))


