"""modulo de serializers do app emitentes"""
from rest_framework.serializers import ModelSerializer

from api.emitentes.models import EmitenteModel


class EmitenteSerializer(ModelSerializer):
    """classe responsavel pela serialização do emitente"""
    class Meta:
        model = EmitenteModel
        fields = '__all__'
