from api.emitentes.models import EmitenteModel
from domain.entities import Emitente
from domain.repositories import EmitenteRepository


class DjangoEmitenteRepository(EmitenteRepository):
    def busca_por_id(self, id):
        emitente_model = EmitenteModel.objects.get(id=id)

        emitente = Emitente.Factory.cria(id=emitente_model.id,
                                         nome=emitente_model.nome,
                                         endereco=emitente_model.endereco,
                                         telefone=emitente_model.telefone)
        return emitente
