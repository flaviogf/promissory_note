"""modulo de models do app emitentes"""

import uuid

from django.db import models


class EmitenteData(models.Model):
    """classe responsavel pela representação do emitente no banco de dados"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=25)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'emitente'
