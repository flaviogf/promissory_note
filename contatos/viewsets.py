from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from rest_framework.viewsets import ModelViewSet

from contatos.models import Contato, Endereco
from contatos.serializers import ContatoSerializer, EnderecoSerializer


class ContatoViewSet(ModelViewSet):
    serializer_class = ContatoSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def get_queryset(self):
        return Contato.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @action(methods=("get", "post"), detail=True)
    def endereco(self, request, pk):
        if request.method == "POST":
            data = request.data.copy()
            data["contato"] = pk
            serializer = EnderecoSerializer(data=data)
            if serializer.is_valid():
                endereco = serializer.save()
                serializer = EnderecoSerializer(endereco)
                return Response(serializer.data, status=HTTP_201_CREATED)

            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        if request.method == "GET":
            try:
                endereco = Endereco.objects.get(contato__contato_id=pk)
                serializer = EnderecoSerializer(endereco)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response(status=HTTP_404_NOT_FOUND)
