from rest_framework.viewsets import ModelViewSet

from api.emitentes.models import EmitenteModel
from api.emitentes.serializers import EmitenteSerializer


class EmitenteViewSet(ModelViewSet):
    queryset = EmitenteModel.objects.all()
    serializer_class = EmitenteSerializer
