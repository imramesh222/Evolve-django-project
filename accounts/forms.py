from django import forms


class LoginForm(forms.Form):
  username=forms.CharField(max_length=200)
  password=forms.CharField(max_length=200,widget=forms.PasswordInput)
