from datetime import date

from django.db import models

from contas.models import Conta
from contatos.models import Contato
from enderecos.models import Endereco
from shared.models import Model


class Promisoria(Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contas = models.ManyToManyField(Conta)
    data_recebimento = models.DateField(blank=True, null=True)
    recebida = models.BooleanField(default=False)

    class Meta:
        ordering = ('criado_em', )

    def __str__(self):
        mensagem = '(recebida)' if self.recebida else '(não recebida)'
        return f'contas {self.quantidade_de_contas} {mensagem}'

    @property
    def quantidade_de_contas(self):
        return self.contas.count()

    def adiciona_conta(self, conta):
        self.contas.add(conta)

    def baixa(self):
        for it in self.contas.all():
            it.recebe()

        self.recebida = True
        self.data_recebimento = date.today()
        self.save()
