from django.test import TestCase

from usuarios.forms import CadastroUsuarioForm


class TestCadastroUsuarioForm(TestCase):
    def test_cadastro_usuario_form_is_valid(self):
        request = {
            'username': 'flaviogf',
            'password1': 'teste123!',
            'password2': 'teste123!',
        }

        form = CadastroUsuarioForm(request)

        self.assertTrue(form.is_valid())
