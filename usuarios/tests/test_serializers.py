from django.contrib.auth import get_user_model
from django.test import TestCase

from usuarios.serializers import LoginSerializer, RegistraUsuarioSerializer


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

    def test_registra_usuario_serializer_create(self):
        request = {
            'username': 'flavio',
            'password1': 'teste123!',
            'password2': 'teste123!',
        }

        usuario = RegistraUsuarioSerializer().create(validated_data=request)

        self.assertIsInstance(usuario, get_user_model())

    def test_registra_usuario_serializer_save(self):
        request = {
            'username': 'flavio',
            'password1': 'teste123!',
            'password2': 'teste123!',
        }

        serializer = RegistraUsuarioSerializer(data=request)

        serializer.save()

        total_usuarios = get_user_model().objects.count()

        self.assertEqual(1, total_usuarios)

    def test_registra_usuario_serializer_is_valid_false_username_existente(
            self):
        usuario = get_user_model().objects.create(username='flavio')
        usuario.set_password('teste123!')
        usuario.save()

        request = {
            'username': 'flavio',
            'password1': 'teste123!',
            'password2': 'teste123!',
        }

        serializer = RegistraUsuarioSerializer(data=request)

        self.assertFalse(serializer.is_valid())


class LoginSerializerTest(TestCase):
    def test_login_serializer_init(self):
        request = {'username': 'flavio', 'password': 'teste123!'}

        serializer = LoginSerializer(data=request)

        self.assertIsInstance(serializer, LoginSerializer)

    def test_login_serializer_is_valid_true(self):
        usuario = get_user_model().objects.create(username='flavio')
        usuario.set_password('teste123!')
        usuario.save()

        request = {'username': 'flavio', 'password': 'teste123!'}

        serializer = LoginSerializer(data=request)

        self.assertTrue(serializer.is_valid())

    def test_login_serializer_is_valid_false(self):
        usuario = get_user_model().objects.create(username='flavio')
        usuario.set_password('teste123!')
        usuario.save()

        request = {'username': 'flavio', 'password': 'teste123'}

        serializer = LoginSerializer(data=request)

        self.assertFalse(serializer.is_valid())

    def test_login_serializer_get_token(self):
        usuario = get_user_model().objects.create(username='flavio')
        usuario.set_password('teste123!')
        usuario.save()

        request = {'username': 'flavio', 'password': 'teste123!'}

        serializer = LoginSerializer(data=request)

        self.assertIsInstance(serializer.get_token(), str)

    def test_login_serializer_get_token_invalido(self):
        usuario = get_user_model().objects.create(username='flavio')
        usuario.set_password('teste123!')
        usuario.save()

        request = {'username': 'flavio', 'password': 'teste123'}

        serializer = LoginSerializer(data=request)

        self.assertIsNone(serializer.get_token())
