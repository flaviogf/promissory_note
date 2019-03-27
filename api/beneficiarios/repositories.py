from api.beneficiarios.models import BeneficiarioModel
from domain.entities import Beneficiario
from domain.repositories import BeneficiarioRepository


class DjangoBeneficiarioRepository(BeneficiarioRepository):
    def busca_por_id(self, id):
        beneficiario_model = BeneficiarioModel.objects.get(id=id)

        beneficiario = Beneficiario.Factory.cria(id=beneficiario_model.id,
                                                 nome=beneficiario_model.nome,
                                                 endereco=beneficiario_model.endereco,
                                                 telefone=beneficiario_model.telefone)
        return beneficiario
