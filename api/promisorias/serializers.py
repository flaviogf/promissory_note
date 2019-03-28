from rest_framework.serializers import ModelSerializer

from api.promisorias.models import PromisoriaModel


class PromisoriaSerializer(ModelSerializer):
    class Meta:
        model = PromisoriaModel
        fields = '__all__'
