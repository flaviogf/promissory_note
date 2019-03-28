from django.db import models

from api.beneficiarios.models import BeneficiarioModel
from api.contas.models import ContaModel
from api.core.models import Model
from api.emitentes.models import EmitenteModel


class PromisoriaModel(Model):
    emitente = models.ForeignKey(EmitenteModel,
                                 on_delete=models.SET_NULL,
                                 blank=False,
                                 null=True)
    beneficiario = models.ForeignKey(BeneficiarioModel,
                                     on_delete=models.SET_NULL,
                                     blank=False,
                                     null=True)
    contas = models.ManyToManyField(ContaModel)
    data_recebimento = models.DateTimeField(blank=True,
                                            null=True)
    recebida = models.BooleanField(default=False)

    class Meta:
        db_table = 'promisoria'
        ordering = ('criado_em',)
