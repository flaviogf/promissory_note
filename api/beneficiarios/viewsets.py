from rest_framework.viewsets import ModelViewSet

from api.beneficiarios.models import BeneficiarioModel
from api.beneficiarios.serializers import BeneficiarioSerializer


class BeneficiarioViewSet(ModelViewSet):
    queryset = BeneficiarioModel.objects.all()
    serializer_class = BeneficiarioSerializer
