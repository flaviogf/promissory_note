import uuid

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.promisorias.models import PromisoriaModel
from api.promisorias.serializers import PromisoriaSerializer
from domain.commands import EmitirPromisoriaCommand
from infra.ioc import get_emitir_promisoria_handler


class PromisoriaViewSet(ModelViewSet):
    queryset = PromisoriaModel.objects.all()
    serializer_class = PromisoriaSerializer

    @action(detail=False,
            methods=['POST'],
            url_path='emite',
            url_name='emite')
    def emite_promisoria(self, request):
        handler = get_emitir_promisoria_handler()
        command = EmitirPromisoriaCommand()
        command.id_emitente = self._get_id_emitente(
            request.data.get('emitente'))
        command.id_beneficario = self._get_id_beneficiario(
            request.data.get('beneficiario'))
        command.id_contas = self._get_id_contas(
            request.data.get('contas'))
        result = handler.handle(command)
        return Response(result.mensagem, status=HTTP_200_OK)

    def _get_id_emitente(self, emitente):
        return uuid.UUID(emitente)

    def _get_id_beneficiario(self, beneficiario):
        return uuid.UUID(beneficiario)

    def _get_id_contas(self, contas):
        return [uuid.UUID(contas)] if isinstance(contas, str) else [uuid.UUID(it) for it in contas]
