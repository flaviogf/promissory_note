from rest_framework import serializers

from contatos.models import Contato, Endereco
from infra.mixins import ErrorArrayMixin
from usuarios.serializers import UsuarioSerializer


class ContatoSerializer(ErrorArrayMixin, serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Contato
        fields = "__all__"
        extra_kwargs = {
            "nome": {
                "error_messages": {
                    "required": "nome invalido",
                    "blank": "nome invalido",
                    "null": "nome invalido",
                }
            },
            "email": {
                "error_messages": {
                    "required": "email invalido",
                    "blank": "email invalido",
                    "null": "email invalido",
                }
            },
            "telefone": {
                "error_messages": {
                    "required": "telefone invalido",
                    "blank": "telefone invalido",
                    "null": "telefone invalido",
                }
            },
        }


class EnderecoSerializer(ErrorArrayMixin, serializers.ModelSerializer):
    class Meta:
        model = Endereco
        exclude = ("contato",)
        extra_kwargs = {
            "contato": {
                "error_messages": {
                    "required": "contato invalido",
                    "blank": "contato invalido",
                    "null": "contato invalido",
                }
            },
            "cep": {
                "error_messages": {
                    "required": "cep invalido",
                    "blank": "cep invalido",
                    "null": "cep invalido",
                }
            },
            "rua": {
                "error_messages": {
                    "required": "rua invalida",
                    "blank": "rua invalida",
                    "null": "rua invalida",
                }
            },
            "bairro": {
                "error_messages": {
                    "required": "bairro invalido",
                    "blank": "bairro invalido",
                    "null": "bairro invalido",
                }
            },
            "numero": {
                "error_messages": {
                    "required": "numero invalido",
                    "blank": "numero invalido",
                    "null": "numero invalido",
                }
            },
        }
