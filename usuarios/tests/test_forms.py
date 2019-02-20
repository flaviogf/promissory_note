from django.contrib.auth import get_user_model
from django.test import TestCase

from usuarios.forms import LoginForm, RegistrarUsuarioForm


class TestRegistarUsuarioForm(TestCase):
    def test_registrar_usuario_form_is_valid_true(self):
        request = {
            'username': 'flaviogf',
            'password1': 'teste123!',
            'password2': 'teste123!',
        }

        form = RegistrarUsuarioForm(request)

        self.assertTrue(form.is_valid())


class TestLoginForm(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create(username='flavio')
        self.usuario.set_password('teste123!')
        self.usuario.save()

    def test_login_form_is_valid_true(self):
        request = {'username': 'flavio', 'password': 'teste123!'}

        form = LoginForm(data=request)

        self.assertTrue(form.is_valid())
