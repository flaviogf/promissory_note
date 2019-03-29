import uuid

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.promisorias.models import PromisoriaModel
from api.promisorias.serializers import PromisoriaSerializer
from domain.commands import EmitirPromisoriaCommand
from ioc import get_emitir_promisoria_handler


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
        command.id_emitente = uuid.UUID(request.data['emitente'])
        command.id_beneficario = uuid.UUID(request.data['beneficiario'])
        command.id_contas = [uuid.UUID(it) for it in request.data['contas']]
        result = handler.handle(command)
        return Response(result.mensagem, status=HTTP_200_OK)
