from django.db import models

from api.core.models import Model


class BeneficiarioModel(Model):
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=25)

    class Meta:
        db_table = 'beneficiario'
