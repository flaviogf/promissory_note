from rest_framework.serializers import ModelSerializer

from api.emitentes.models import EmitenteModel


class EmitenteSerializer(ModelSerializer):
    class Meta:
        model = EmitenteModel
        fields = '__all__'
