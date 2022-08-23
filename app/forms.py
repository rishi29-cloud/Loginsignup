from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegister(UserCreationForm):
    first_name = forms.CharField(
        label='First name: ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        label='Last name: ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        label='Username: ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, label='Email: ', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Create Password: ', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password: ', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    Address = forms.CharField(label='Address: ', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    City = forms.CharField(label='City: ', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Pincode = forms.IntegerField(label='Pincode: ', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1',
                  'password2', 'Address', 'City', 'Pincode', 'State']
        widgets = {'State': forms.Select(attrs={'class': 'form-control'})}


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
