"""modulo de serializers do app emitentes"""
from rest_framework.serializers import ModelSerializer

from api.emitentes.models import EmitenteData


class EmitenteSerializer(ModelSerializer):
    """classe responsavel pela serialização do emitente"""
    class Meta:
        model = EmitenteData
        fields = '__all__'
