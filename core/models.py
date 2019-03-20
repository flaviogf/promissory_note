from django.db import models

from contas.models import Conta
from contatos.models import Contato
from enderecos.models import Endereco
from shared.models import Model


class Promisoria(Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contas = models.ManyToManyField(Conta)

    class Meta:
        ordering = ('criado_em', )
