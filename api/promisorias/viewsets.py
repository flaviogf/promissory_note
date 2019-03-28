from rest_framework.viewsets import ModelViewSet

from api.promisorias.models import PromisoriaModel
from api.promisorias.serializers import PromisoriaSerializer


class PromisoriaViewSet(ModelViewSet):
    queryset = PromisoriaModel.objects.all()
    serializer_class = PromisoriaSerializer
