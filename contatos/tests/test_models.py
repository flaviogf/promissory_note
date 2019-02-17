from django.test import TestCase

from contatos.models import AtividadeContato, Contato, Endereco


class TestContato(TestCase):
    def test_contato_init(self):
        contato = Contato(
            nome='Flavio', email='flavio@email.com', telefone='016999999999')

        self.assertEqual('Flavio', contato.nome)
        self.assertEqual('flavio@email.com', contato.email)
        self.assertEqual('016999999999', contato.telefone)

    def test_contato_str(self):
        contato = Contato(
            nome='Flavio', email='flavio@email.com', telefone='016999999999')

        self.assertEqual('Flavio', contato.__str__())


class TestEndereco(TestCase):
    def test_endereco_init(self):
        contato = Contato(
            nome='Flavio', email='flavio@email.com', telefone='016999999999')

        endereco = Endereco(
            contato=contato,
            cep='14400000',
            rua='rua',
            bairro='bairro',
            numero='12345')

        self.assertEqual(contato.nome, endereco.contato.nome)
        self.assertEqual('14400000', endereco.cep)
        self.assertEqual('rua', endereco.rua)
        self.assertEqual('bairro', endereco.bairro)
        self.assertEqual('12345', endereco.numero)

    def test_endereco_str(self):
        contato = Contato(
            nome='Flavio', email='flavio@email.com', telefone='016999999999')

        endereco = Endereco(
            contato=contato,
            cep='14400000',
            rua='rua',
            bairro='bairro',
            numero='12345')

        self.assertEqual('rua - bairro', endereco.__str__())


class TestAtividadeContato(TestCase):
    def test_atividade_contato_init(self):
        contato = Contato(
            nome='Flavio', email='flavio@email.com', telefone='016999999999')

        mensagem = f'Contato {contato.nome} criado'

        atividade_contato = AtividadeContato(
            mensagem=mensagem,
            status_atual=contato.__dict__,
            status_anterior=None)

        self.assertEqual(mensagem, atividade_contato.mensagem)
        self.assertEqual(contato.__dict__, atividade_contato.status_atual)
        self.assertEqual(None, atividade_contato.status_anterior)
