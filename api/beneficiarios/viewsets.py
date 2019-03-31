from rest_framework.viewsets import ModelViewSet

from api.beneficiarios.models import Beneficiario
from api.beneficiarios.serializers import BeneficiarioSerializer


class BeneficiarioViewSet(ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
