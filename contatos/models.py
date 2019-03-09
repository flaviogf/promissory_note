import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contato(models.Model):
    contato_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome = models.CharField(max_length=100)

    email = models.EmailField()

    telefone = models.CharField(max_length=12)

    usuario = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="usuario", null=True
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ["-criado_em"]

    def __str__(self):
        return self.nome


@receiver(post_save, sender=Contato, dispatch_uid="post_save_contato")
def post_save_contato(sender, instance, *args, **kwargs):
    HistoricoContato.objects.create(
        contato=instance,
        nome=instance.nome,
        email=instance.email,
        telefone=instance.telefone,
    )


class Endereco(models.Model):
    contato = models.OneToOneField(
        Contato, on_delete=models.CASCADE, primary_key=True, related_name="endereco"
    )

    cep = models.CharField(max_length=9)

    rua = models.CharField(max_length=100)

    bairro = models.CharField(max_length=100)

    numero = models.CharField(max_length=5)

    criado_em = models.DateTimeField(auto_now_add=True, null=True)

    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.rua} - {self.bairro}"


@receiver(post_save, sender=Endereco, dispatch_uid="post_save_endereco")
def post_save_endereco(sender, instance, *args, **kwargs):
    HistoricoEndereco.objects.create(
        endereco=instance,
        cep=instance.cep,
        rua=instance.rua,
        bairro=instance.bairro,
        numero=instance.numero,
    )


class HistoricoContato(models.Model):
    contato = models.ForeignKey(
        Contato, on_delete=models.CASCADE, related_name="historicos"
    )

    nome = models.CharField(max_length=100)

    email = models.EmailField()

    telefone = models.CharField(max_length=12)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Histórico Contato"
        verbose_name_plural = "Históricos Contatos"
        ordering = ["-atualizado_em"]


class HistoricoEndereco(models.Model):
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, related_name="historicos"
    )

    cep = models.CharField(max_length=9)

    rua = models.CharField(max_length=100)

    bairro = models.CharField(max_length=100)

    numero = models.CharField(max_length=5)

    criado_em = models.DateTimeField(auto_now_add=True, null=True)

    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Histórico Endereço"
        verbose_name_plural = "Históricos Endereços"
        ordering = ["-atualizado_em"]
