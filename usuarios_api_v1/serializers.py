import re

from rest_framework import serializers


class RegistraUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate_password1(self, value):
        regex = r'^((?=.*[a-z])(?=.*\d)(?=.*[\)\(*!])).{9,}$'

        if not re.match(regex, value):
            raise serializers.ValidationError('senha fraca')
        return value

    def validate(self, data):
        super().validate(data)

        if data['password1'] != data['password2']:
            raise serializers.ValidationError('senhas são diferentes')

        return data
