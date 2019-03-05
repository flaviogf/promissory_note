from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contatos.models import Contato
from contatos.serializers import ContatoSerializer
from infra.decorators import log_request


class ContatoAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(log_request)
    def get(self, request, contato_id):
        contato = get_object_or_404(
            Contato, usuario=request.user, contato_id=contato_id)
        serializer = ContatoSerializer(contato)
        return Response(serializer.data)
