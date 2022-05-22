from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=False)
    email = forms.EmailField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UpdateUserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        model = UserProfile
        fields = ['avatar']