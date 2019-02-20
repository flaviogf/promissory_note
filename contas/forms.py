from django.forms import forms
from contas.models import Conta


class ContaForm(forms.Form):
    class Meta:
        model = Conta
        fields = ('contato', 'valor', 'data_recebimento_esperado')
