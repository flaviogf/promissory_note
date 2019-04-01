from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from api.promissorias.serializers import SolicitarPromissoriaSerializer
from domain.core.commands import SolicitarPromissoriaCommand
from infra.ioc import get_solicitar_promissoria_handler


class PromissoriaViewSet(ViewSet):

    def create(self, request):
        serializer = SolicitarPromissoriaSerializer(data=request.data)

        if serializer.is_valid():
            handler = get_solicitar_promissoria_handler()

            command = SolicitarPromissoriaCommand(numero=serializer.validated_data['numero'],
                                                  data_vencimento=serializer.validated_data['data_vencimento'],
                                                  valor=serializer.validated_data['valor'],
                                                  id_beneficiario=serializer.validated_data['id_beneficiario'],
                                                  id_emitente=serializer.validated_data['id_emitente'])

            handler.handle(command)

            return Response(status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
