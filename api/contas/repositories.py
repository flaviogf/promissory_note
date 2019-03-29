from api.contas.models import ContaModel
from domain.entities import Conta
from domain.repositories import ContaRepository


class DjangoContaRepository(ContaRepository):
    def lista_por_id(self, ids):
        contas_model = ContaModel.objects.filter(id__in=ids)
        contas = (Conta.Factory.cria(id=it.id,
                                     descricao=it.descricao,
                                     valor=it.valor,
                                     data_recebimento=it.data_recebimento,
                                     recebida=it.recebida) for it in contas_model)
        return contas
