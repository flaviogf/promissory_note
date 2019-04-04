from api.emitentes.models import Emitente as EmitenteData
from domain.promissoria.entities import Emitente
from domain.promissoria.repositories import EmitenteRepository


class DjangoEmitenteRepository(EmitenteRepository):
    def busca_por_id(self, id):
        emitente = EmitenteData.objects.get(id=id)
        return Emitente.Factory.cria(id=emitente.id,
                                     nome=emitente.nome,
                                     documento=emitente.documento,
                                     email=emitente.email,
                                     endereco=emitente.endereco)
