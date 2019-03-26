"""modulo de models do app emitentes"""
from django.db import models

from api.core.models import Model


class EmitenteModel(Model):
    """classe responsavel pela representação do emitente no banco de dados"""
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=25)

    class Meta:
        db_table = 'emitente'
