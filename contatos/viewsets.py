from rest_framework.viewsets import ModelViewSet

from contatos.models import Contato
from contatos.serializers import ContatoSerializer


class ContatoViewSet(ModelViewSet):
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()
