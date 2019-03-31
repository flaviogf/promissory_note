from rest_framework.serializers import ModelSerializer

from api.beneficiarios.models import Beneficiario


class BeneficiarioSerializer(ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = '__all__'
