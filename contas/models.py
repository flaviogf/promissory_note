from datetime import datetime
from uuid import uuid4

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from contatos.models import Contato

# Create your models here.


class Conta(models.Model):
    conta_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    contato = models.ForeignKey(
        Contato, on_delete=models.CASCADE, related_name="contas"
    )

    valor = models.DecimalField(max_digits=8, decimal_places=2)

    data_recebimento_esperado = models.DateField()

    data_recebimento = models.DateField(blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["data_recebimento_esperado"]

    @property
    def recebida(self):
        return self.data_recebimento is not None

    @property
    def vencida(self):
        return (
            self.data_recebimento_esperado < datetime.now().date() and not self.recebida
        )

    def recebe(self, data_recebimento=None):
        data_recebimento = data_recebimento or datetime.now()
        self.data_recebimento = data_recebimento


@receiver(post_save, sender=Conta, dispatch_uid="post_save_contas")
def post_save_conta(sender, instance, **kwargs):
    HistoricoConta.objects.create(
        conta=instance,
        valor=instance.valor,
        data_recebimento_esperado=instance.data_recebimento_esperado,
        data_recebimento=instance.data_recebimento,
    )


class HistoricoConta(models.Model):
    conta = models.ForeignKey(
        Conta, on_delete=models.CASCADE, related_name="historicos"
    )

    valor = models.DecimalField(max_digits=8, decimal_places=2)

    data_recebimento_esperado = models.DateField()

    data_recebimento = models.DateField(blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    @property
    def recebida(self):
        return self.data_recebimento is not None

    class Meta:
        ordering = ["-atualizado_em"]
