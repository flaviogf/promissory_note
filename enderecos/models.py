from uuid import uuid4

from django.db import models
from django.utils import timezone

from shared.models import Model


class Endereco(Model):
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    numero = models.CharField(max_length=9)

    class Meta:
        ordering = ('-criado_em', )
