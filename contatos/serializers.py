from rest_framework import serializers

from contatos.models import Contato, Endereco


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        exclude = ('usuario',)


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        exclude = ('contato',)
