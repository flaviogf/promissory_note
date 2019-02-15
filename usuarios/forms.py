from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label='Confirmar senha',
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta(UserCreationForm.Meta):
        labels = {
            'username': 'Username',
        }
