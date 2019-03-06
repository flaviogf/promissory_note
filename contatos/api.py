from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from contatos.models import Contato
from contatos.serializers import ContatoSerializer, EnderecoSerializer
from infra.decorators import log_request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class ContatoAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(log_request)
    def get(self, request, contato_id):
        contato = get_object_or_404(
            Contato, usuario=request.user, contato_id=contato_id
        )
        serializer = ContatoSerializer(contato)
        return Response(serializer.data)


class ContatosAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        contato_serializer = ContatoSerializer(data=request.data or None)
        endereco_serializer = EnderecoSerializer(data=request.data or None)

        contato_valido = contato_serializer.is_valid()
        endereco_valido = endereco_serializer.is_valid()

        if contato_valido and endereco_valido:
            contato = contato_serializer.save(usuario=request.user)
            endereco = endereco_serializer.save(contato=contato)
            contato_serializer = ContatoSerializer(contato)
            return Response(contato_serializer.data, status=HTTP_201_CREATED)

        errors = contato_serializer.errors + endereco_serializer.errors

        return Response(errors, HTTP_400_BAD_REQUEST)
