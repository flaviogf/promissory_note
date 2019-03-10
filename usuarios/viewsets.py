from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework.viewsets import ViewSet

from infra.decorators import log_request
from usuarios.serializers import (
    LoginSerializer,
    RegistraUsuarioSerializer,
    UsuarioSerializer,
)


class UsuarioViewSet(ViewSet):
    @action(methods=("post",), detail=False)
    @method_decorator(log_request)
    def registra(self, request):
        serializer = RegistraUsuarioSerializer(data=request.data)

        if serializer.is_valid():
            usuario = serializer.save()
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(methods=("post",), detail=False)
    @method_decorator(log_request)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.get_token())

        return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)
