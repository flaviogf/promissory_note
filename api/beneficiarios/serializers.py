from rest_framework.serializers import ModelSerializer

from api.beneficiarios.models import BeneficiarioModel


class BeneficiarioSerializer(ModelSerializer):
    class Meta:
        model = BeneficiarioModel
        fields = '__all__'
