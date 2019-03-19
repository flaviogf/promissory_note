from datetime import date
from uuid import uuid4

from django.db import models
from django.utils import timezone

from shared.models import Model


class Conta(Model):
    descricao = models.TextField(max_length=500)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_recebimento = models.DateField(default=date.today)
    recebida = models.BooleanField(default=False)

    class Meta:
        ordering = ('data_recebimento', )

    def __str__(self):
        mensagem_status = '(não recebido)' if not self.recebida else '(recebido)'
        return f'R$ {self.valor} {mensagem_status}'
