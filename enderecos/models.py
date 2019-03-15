from uuid import uuid4

from django.db import models
from django.utils import timezone


class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    numero = models.CharField(max_length=9)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-criado_em', )

    def __str__(self):
        return f'{self.rua} - {self.numero} - {self.bairro}'
