from django.db import models

from api.core.models import Model


class ContaModel(Model):
    descricao = models.TextField(max_length=500)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_recebimento = models.DateTimeField(null=True, blank=True)
    recebida = models.BooleanField(default=False)

    class Meta:
        db_table = 'conta'
