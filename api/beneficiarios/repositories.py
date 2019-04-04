from api.beneficiarios.models import Beneficiario as BeneficiarioData
from domain.promissoria.entities import Beneficiario
from domain.promissoria.repositories import BeneficiarioRepository


class DjangoBeneficiarioRepository(BeneficiarioRepository):
    def busca_por_id(self, id):
        beneficiario = BeneficiarioData.objects.get(id=id)
        return Beneficiario.Factory.cria(id=beneficiario.id,
                                         nome=beneficiario.nome,
                                         documento=beneficiario.documento,
                                         email=beneficiario.email)
