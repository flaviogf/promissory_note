"""modulo dos repositorios do app promisorias"""
from api.beneficiarios.models import BeneficiarioModel
from api.contas.models import ContaModel
from api.emitentes.models import EmitenteModel
from api.promisorias.models import PromisoriaModel
from domain.repositories import PromisoriaRepository


class DjangoPromisoriaRepository(PromisoriaRepository):
    """classe responsavel por buscar informacoes das promisorias"""
    def insere(self, promisoria):
        """insere uma promisoria"""
        id_emitente = promisoria.emitente.id
        emitente = EmitenteModel.objects.get(id=id_emitente)
        id_contas = [it.id for it in promisoria.contas]
        contas = ContaModel.objects.filter(id__in=id_contas)
        promisoria = PromisoriaModel.objects.create(id=promisoria.id,
                                                    emitente=emitente)
        promisoria.contas.set(contas)
