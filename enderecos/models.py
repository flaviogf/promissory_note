from uuid import uuid4

from django.db import models


class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    numero = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.rua} - {self.numero} - {self.bairro}'
