from rest_framework.serializers import ModelSerializer

from api.contas.models import ContaModel


class ContaSerializer(ModelSerializer):
    class Meta:
        model = ContaModel
        fields = '__all__'
