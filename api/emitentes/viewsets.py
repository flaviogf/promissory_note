from rest_framework.viewsets import ModelViewSet

from api.emitentes.models import Emitente
from api.emitentes.serializers import EmitenteSerializer


class EmitenteViewSet(ModelViewSet):
    queryset = Emitente.objects.all()
    serializer_class = EmitenteSerializer
