from django.test import TestCase

from usuarios_api_v1.serializers import RegistraUsuarioSerializer


class TestRegistraUsuarioSerializer(TestCase):
    def test_registra_usuario_serializer_is_valid_true(self):
        request = {
            'username': 'flavio',
            'password1': 'teste123!',
            'password2': 'teste123!',
        }

        serializer = RegistraUsuarioSerializer(data=request)

        self.assertTrue(serializer.is_valid())

    def test_registra_usuario_serializer_is_valid_false(self):
        serializer = RegistraUsuarioSerializer(data={})

        self.assertFalse(serializer.is_valid())

    def test_registra_usuario_serializer_is_valid_false_senhas_diferentes(
            self):
        request = {
            'username': 'flavio',
            'password1': 'teste123!',
            'password2': 'teste123',
        }

        serializer = RegistraUsuarioSerializer(data=request)

        self.assertFalse(serializer.is_valid())

    def test_registra_usuario_serializer_is_valid_false_senha_fraca_somente_caracteres(
            self):
        request = {
            'username': 'flavio',
            'password1': 'teste',
            'password2': 'teste'
        }

        serializer = RegistraUsuarioSerializer(data=request)

        self.assertFalse(serializer.is_valid())
