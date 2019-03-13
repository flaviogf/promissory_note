from uuid import uuid4

from django.db import models


class Contato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
