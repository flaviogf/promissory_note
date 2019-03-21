from rest_framework.serializers import HyperlinkedRelatedField, ModelSerializer

from contas.models import Conta
from contatos.models import Contato
from core.models import Promisoria
from enderecos.models import Endereco


class PromisoriaSerializer(ModelSerializer):
    contato = HyperlinkedRelatedField(
        queryset=Contato.objects.all(), view_name='contato-detail')
    endereco = HyperlinkedRelatedField(
        queryset=Endereco.objects.all(), view_name='endereco-detail')
    contas = HyperlinkedRelatedField(
        queryset=Conta.objects.all(), view_name='conta-detail', many=True)

    class Meta:
        model = Promisoria
        fields = '__all__'
