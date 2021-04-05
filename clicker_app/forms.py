from django import forms
from clicker_app.models import User, Account


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('image',)