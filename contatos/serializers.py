from rest_framework.serializers import ModelSerializer

from contatos.models import Contato


class ContatoSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'
