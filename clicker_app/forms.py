from django import forms
from clicker_app.models import User, Account


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': '',
            'email': '',
            'password': '',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email: john@doe.com'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class ImageUpload(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('image', )
