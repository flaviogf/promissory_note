import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Contato(models.Model):
    contato_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    nome = models.CharField(max_length=100)

    email = models.EmailField()

    telefone = models.CharField(max_length=12)

    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='usuario', null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    contato = models.OneToOneField(
        Contato,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='endereco')

    cep = models.CharField(max_length=9)

    rua = models.CharField(max_length=100)

    bairro = models.CharField(max_length=100)

    numero = models.CharField(max_length=5)

    criado_em = models.DateTimeField(auto_now_add=True, null=True)

    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f'{self.rua} - {self.bairro}'
