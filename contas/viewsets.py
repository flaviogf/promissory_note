from rest_framework.viewsets import ModelViewSet

from contas.models import Conta
from contas.serializers import ContaSerializer


class ContaViewSet(ModelViewSet):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()
