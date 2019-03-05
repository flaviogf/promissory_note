from rest_framework import serializers

from contatos.models import Contato, Endereco
from infra.mixins import ErrorArrayMixin


class ContatoSerializer(ErrorArrayMixin, serializers.ModelSerializer):
    class Meta:
        model = Contato
        exclude = ('usuario',)


class EnderecoSerializer(ErrorArrayMixin, serializers.ModelSerializer):
    class Meta:
        model = Endereco
        exclude = ('contato',)
