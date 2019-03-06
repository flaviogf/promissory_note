from django.utils.decorators import method_decorator

from infra.decorators import log_request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework.views import APIView
from usuarios.serializers import LoginSerializer, RegistraUsuarioSerializer

# Create your views here.


class UsuarioAPIView(APIView):
    @method_decorator(log_request)
    def post(self, request):
        serializer = RegistraUsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    @method_decorator(log_request)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.get_token())

        return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)
