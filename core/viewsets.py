from rest_framework.viewsets import ModelViewSet

from core.models import Promisoria
from core.serializers import PromisoriaSerializer


class PromisoriaViewSet(ModelViewSet):
    serializer_class = PromisoriaSerializer
    queryset = Promisoria.objects.all()
