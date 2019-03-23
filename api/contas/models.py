import uuid

from django.db import models


class ContaData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=500)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_recebimento = models.DateTimeField(blank=True, null=True)
    recebida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contas'
