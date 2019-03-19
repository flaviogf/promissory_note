from uuid import uuid4

from django.db import models


class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
