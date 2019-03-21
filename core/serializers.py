from rest_framework.serializers import HyperlinkedRelatedField, ModelSerializer

from contas.models import Conta
from contatos.models import Contato
from core.models import Promisoria
from enderecos.models import Endereco


class PromisoriaSerializer(ModelSerializer):
    class Meta:
        model = Promisoria
        fields = '__all__'
