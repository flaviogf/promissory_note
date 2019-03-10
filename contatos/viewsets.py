from django.db import transaction
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from contatos.models import Contato, Endereco
from contatos.serializers import ContatoSerializer, EnderecoSerializer


class ContatoViewSet(ModelViewSet):
    serializer_class = ContatoSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def get_queryset(self):
        return Contato.objects.filter(usuario=self.request.user)

    @action(methods=["post"], detail=False)
    @method_decorator(transaction.atomic)
    def com_endereco(self, request):
        contato_serializer = ContatoSerializer(data=request.data)
        if not contato_serializer.is_valid():
            transaction.set_rollback(True)
            return Response(contato_serializer.errors, status=HTTP_400_BAD_REQUEST)

        contato = contato_serializer.save(usuario=request.user)

        endereco_data = request.data.copy()
        endereco_data["contato"] = contato.contato_id
        endereco_serializer = EnderecoSerializer(data=endereco_data)
        if not endereco_serializer.is_valid():
            transaction.set_rollback(True)
            return Response(endereco_serializer.errors, status=HTTP_400_BAD_REQUEST)

        endereco_serializer.save(contato=contato)

        contato_serializer = ContatoSerializer(contato)
        return Response(contato_serializer.data, status=HTTP_201_CREATED)
