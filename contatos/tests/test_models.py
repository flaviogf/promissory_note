from django.test import TestCase

from contatos.models import Contato, Endereco, HistoricoContato, HistoricoEndereco


class TestContato(TestCase):
    def test_contato_create(self):
        contato = Contato.objects.create(
            nome="Flavio", email="flavio@email.com", telefone="016999999999"
        )

        self.assertEqual("Flavio", contato.nome)
        self.assertEqual("flavio@email.com", contato.email)
        self.assertEqual("016999999999", contato.telefone)

    def test_contato_str(self):
        contato = Contato.objects.create(
            nome="Flavio", email="flavio@email.com", telefone="016999999999"
        )

        self.assertEqual("Flavio", contato.__str__())


class TestEndereco(TestCase):
    def test_endereco_create(self):
        contato = Contato.objects.create(
            nome="Flavio", email="flavio@email.com", telefone="016999999999"
        )

        endereco = Endereco.objects.create(
            contato=contato, cep="14400000", rua="rua", bairro="bairro", numero="12345"
        )

        self.assertEqual(contato.nome, endereco.contato.nome)
        self.assertEqual("14400000", endereco.cep)
        self.assertEqual("rua", endereco.rua)
        self.assertEqual("bairro", endereco.bairro)
        self.assertEqual("12345", endereco.numero)

    def test_endereco_str(self):
        contato = Contato.objects.create(
            nome="Flavio", email="flavio@email.com", telefone="016999999999"
        )

        endereco = Endereco.objects.create(
            contato=contato, cep="14400000", rua="rua", bairro="bairro", numero="12345"
        )

        self.assertEqual("rua - bairro", endereco.__str__())


class TestHistoricoContato(TestCase):
    def test_historico_contato_create(self):
        contato = Contato.objects.create(
            nome="Flavio", email="flavio@email.com", telefone="016999999999"
        )

        historico_contato = HistoricoContato.objects.create(
            contato=contato,
            nome=contato.nome,
            email=contato.email,
            telefone=contato.telefone,
        )

        self.assertEqual(contato.nome, historico_contato.nome)
        self.assertEqual(contato.email, historico_contato.email)
        self.assertEqual(contato.telefone, historico_contato.telefone)


class TestHistoricoEndereco(TestCase):
    def test_historico_endereco_create(self):
        contato = Contato.objects.create(
            nome="Flavio", email="flavio@email.com", telefone="016999999999"
        )

        endereco = Endereco.objects.create(
            contato=contato, cep="14400000", rua="rua", bairro="bairro", numero="12345"
        )

        historico_endereco = HistoricoEndereco.objects.create(
            endereco=endereco,
            cep=endereco.cep,
            rua=endereco.rua,
            bairro=endereco.bairro,
            numero=endereco.numero,
        )

        self.assertEqual(endereco, historico_endereco.endereco)
        self.assertEqual(endereco.cep, historico_endereco.cep)
        self.assertEqual(endereco.rua, historico_endereco.rua)
        self.assertEqual(endereco.bairro, historico_endereco.bairro)
        self.assertEqual(endereco.numero, historico_endereco.numero)
