from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)


class RegistrarUsuarioForm(UserCreationForm):
    password1 = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput)

    password2 = forms.CharField(
        label="Confirmar senha", strip=False, widget=forms.PasswordInput
    )

    class Meta(UserCreationForm.Meta):
        labels = {"username": "Nome de usuario"}


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="Nome de usuario", widget=forms.TextInput(attrs={"autofocus": True})
    )

    password = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput)
