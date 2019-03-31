from rest_framework.viewsets import ModelViewSet

from api.emitente.models import Emitente
from api.emitente.serializers import EmitenteSerializer


class EmitenteViewSet(ModelViewSet):
    queryset = Emitente.objects.all()
    serializer_class = EmitenteSerializer
