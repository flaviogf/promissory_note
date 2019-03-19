from rest_framework.serializers import ModelSerializer

from core.models import Promisoria


class PromisoriaSerializer(ModelSerializer):
    class Meta:
        model = Promisoria
        fields = '__all__'
