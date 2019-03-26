"""modulo de viewsets do app emitentes"""
from rest_framework.viewsets import ModelViewSet

from api.emitentes.models import EmitenteModel
from api.emitentes.serializers import EmitenteSerializer


class EmitenteViewSet(ModelViewSet):
    """classe responsavel por disponibilizar os endpoints do app emitentes"""
    queryset = EmitenteModel.objects.all()
    serializer_class = EmitenteSerializer
