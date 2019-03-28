from api.beneficiarios.models import BeneficiarioModel
from api.contas.models import ContaModel
from api.emitentes.models import EmitenteModel
from api.promisorias.models import PromisoriaModel
from domain.repositories import PromisoriaRepository


class DjangoPromisoriaRepository(PromisoriaRepository):
    def insere(self, promisoria):
        id_emitente = promisoria.emitente.id
        emitente = EmitenteModel.objects.get(id=id_emitente)
        id_beneficiario = promisoria.beneficiario.id
        beneficiario = BeneficiarioModel.objects.get(id=id_beneficiario)
        id_contas = [it.id for it in promisoria.contas]
        contas = ContaModel.objects.filter(id__in=id_contas)
        promisoria = PromisoriaModel.objects.create(id=promisoria.id,
                                                    emitente=emitente,
                                                    beneficiario=beneficiario)
        promisoria.contas.set(contas)
