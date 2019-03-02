from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from usuarios_api_v1.serializers import RegistraUsuarioSerializer

# Create your views here.


class UsuarioViewSet(ViewSet):
    def create(self, request):
        serializer = RegistraUsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
