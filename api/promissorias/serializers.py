from rest_framework import serializers


class SolicitarPromissoriaSerializer(serializers.Serializer):
    numero = serializers.CharField(max_length=250)
    data_vencimento = serializers.DateTimeField()
    valor = serializers.DecimalField(max_digits=7, decimal_places=2)
    id_beneficiario = serializers.UUIDField()
    id_emitente = serializers.UUIDField()
