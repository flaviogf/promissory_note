import re

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class RegistraUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate_username(self, value):
        try:
            if get_user_model().objects.get(username=value):
                raise serializers.ValidationError('username indisponivel')
        except ObjectDoesNotExist:
            return value

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

    def create(self, validated_data):
        usuario = get_user_model().objects.create(
            username=validated_data['username'])
        usuario.set_password(validated_data['password1'])
        usuario.save()
        return usuario

    def save(self):
        if super().is_valid():
            super().save()
