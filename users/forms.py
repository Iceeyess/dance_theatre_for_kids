from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    """Форма аутентификации"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)


class UserRegistrationForm(UserCreationForm):
    """Форма регистрации"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'phone', 'password1', 'password2', 'username', 'first_name', 'last_name',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }