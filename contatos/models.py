from uuid import uuid4

from django.db import models

from shared.models import Model


class Contato(Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=25)

    class Meta:
        ordering = ('-criado_em', )

    def __str__(self):
        return self.nome
