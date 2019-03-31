from django.db import models

from api.shared.models import Model


class Beneficiario(Model):
    nome = models.CharField(max_length=250)
    documento = models.CharField(max_length=250)
    email = models.EmailField()

    class Meta:
        ordering = ('-criado_em',)
