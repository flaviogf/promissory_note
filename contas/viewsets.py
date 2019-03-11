from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from contas.models import Conta
from contas.serializers import ContaSerializer


class ContaViewSet(ModelViewSet):
    serializer_class = ContaSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def get_queryset(self):
        return Conta.objects.filter(contato__usuario=self.request.user)

    @action(methods=("post",), detail=True)
    def recebe(self, request, pk):
        conta = Conta.objects.get(pk=pk)
        conta.recebe()
        conta.save()
        return Response(status=HTTP_204_NO_CONTENT)
