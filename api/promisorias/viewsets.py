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

    def create(self, request):
        handler = get_emitir_promisoria_handler()
        command = EmitirPromisoriaCommand()
        command.id_emitente = request.data['emitente']
        command.id_beneficario = request.data['beneficiario']
        command.id_contas = request.data['contas']
        result = handler.handle(command)
        return Response(status=HTTP_200_OK)
