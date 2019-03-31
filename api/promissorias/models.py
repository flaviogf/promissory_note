from django.db import models
from django.utils import timezone

from api.beneficiarios.models import Beneficiario
from api.emitentes.models import Emitente
from api.shared.models import Model


class Promissoria(Model):
    numero = models.CharField(max_length=250)
    data_vencimento = models.DateTimeField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.SET_NULL, blank=False, null=True)
    emitente = models.ForeignKey(Emitente, on_delete=models.SET_NULL, blank=False, null=True)
    data_emissao = models.DateTimeField(default=timezone.now)
    recebida = models.BooleanField(default=False)
