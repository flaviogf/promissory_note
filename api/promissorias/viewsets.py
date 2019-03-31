from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from api.promissorias.serializers import SolicitarPromissoriaSerializer


class PromissoriaViewSet(ViewSet):

    def create(self, request):
        serializer = SolicitarPromissoriaSerializer(data=request.data)

        if serializer.is_valid():
            return Response(status=HTTP_200_OK)

        return Response(status=HTTP_400_BAD_REQUEST)
