from rest_framework.viewsets import ModelViewSet

from api.contas.models import ContaModel
from api.contas.serializers import ContaSerializer


class ContaViewSet(ModelViewSet):
    queryset = ContaModel.objects.all()
    serializer_class = ContaSerializer
