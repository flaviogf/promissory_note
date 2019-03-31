import uuid

from django.db import models


class Emitente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=250)
    documento = models.CharField(max_length=250)
    email = models.EmailField()
    endereco = models.CharField(max_length=250)

    class Meta:
        ordering = ('-criado_em',)
