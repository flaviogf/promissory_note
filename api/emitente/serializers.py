from rest_framework.serializers import ModelSerializer

from api.emitente.models import Emitente


class EmitenteSerializer(ModelSerializer):
    class Meta:
        model = Emitente
        fields = '__all__'
