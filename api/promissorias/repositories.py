from api.beneficiarios.models import Beneficiario as BeneficiarioData
from api.emitentes.models import Emitente as EmitenteData
from api.promissorias.models import Promissoria as PromissoriaData
from domain.promissoria.entities import Promissoria
from domain.promissoria.repositories import PromissoriaRepository


class DjangoPromissoriaRepository(PromissoriaRepository):
    def insere(self, promissoria: 'Promissoria'):
        emitente = EmitenteData.objects.get(id=promissoria.emitente.id)
        beneficiario = BeneficiarioData.objects.get(id=promissoria.beneficiario.id)
        PromissoriaData.objects.create(id=promissoria.id,
                                       numero=promissoria.numero,
                                       data_vencimento=promissoria.data_vencimento,
                                       valor=promissoria.valor,
                                       beneficiario=beneficiario,
                                       emitente=emitente)
