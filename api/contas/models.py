from django.db import models

from api.core.models import Model


class ContaModel(Model):
    descricao = models.TextField(max_length=500)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_recebimento = models.DateTimeField(null=True, blank=True)
    recebida = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.valor} {self.descricao[:10]}'

    class Meta:
        db_table = 'conta'
        ordering = ('criado_em',)
