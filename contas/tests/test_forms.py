from datetime import datetime

from django.test import TestCase

from contas.forms import ContaForm
from contatos.models import Contato


class TestContaForm(TestCase):
    def test_conta_form_is_valid_true(self):
        contato = Contato.objects.create(
            nome='Flavio', email='flavio@email.com', telefone='016999999999')

        request = {
            'contato': contato.contato_id,
            'valor': 100.0,
            'data_recebimento_esperado': datetime.now().date()
        }

        form = ContaForm(request)

        self.assertTrue(form.is_valid())
