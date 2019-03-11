import re

from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from infra.mixins import ErrorArrayMixin


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class RegistraUsuarioSerializer(ErrorArrayMixin, serializers.Serializer):
    username = serializers.CharField(
        error_messages={
            "required": "username invalido",
            "null": "username invalido",
            "blank": "username invalido",
        }
    )
    password1 = serializers.CharField(
        error_messages={
            "required": "password1 invalida",
            "null": "password1 invalida",
            "blank": "password1 invalida",
        }
    )
    password2 = serializers.CharField(
        error_messages={
            "required": "password2 invalida",
            "null": "password2 invalida",
            "blank": "password2 invalida",
        }
    )

    def create(self, validated_data):
        usuario = get_user_model().objects.create(username=validated_data["username"])
        usuario.set_password(validated_data["password1"])
        usuario.save()
        return usuario

    def update(self, validated_data):
        pass

    def save(self):
        if super().is_valid():
            return super().save()

    def validate_username(self, value):
        try:
            if get_user_model().objects.get(username=value):
                raise serializers.ValidationError("username indisponivel")
        except ObjectDoesNotExist:
            return value

    def validate_password1(self, value):
        regex = r"^((?=.*[a-z])(?=.*\d)(?=.*[\)\(*!])).{9,}$"

        if not re.match(regex, value):
            raise serializers.ValidationError("senha fraca")
        return value

    def validate(self, data):
        super().validate(data)

        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("senhas são diferentes")

        return data


class LoginSerializer(ErrorArrayMixin, serializers.Serializer):
    username = serializers.CharField(
        error_messages={
            "required": "username invalido",
            "blank": "username invalido",
            "null": "username invalido",
        }
    )
    password = serializers.CharField(
        error_messages={
            "required": "password invalida",
            "blank": "password invalida",
            "null": "password invalida",
        }
    )

    def create(self, validated_data):
        pass

    def update(self, validated_data):
        pass

    def validate(self, data):
        username = data["username"]
        password = data["password"]

        if not authenticate(username=username, password=password):
            raise serializers.ValidationError("usuario nao autenticado")

        return data

    def get_token(self):
        if self.is_valid():
            username = self.validated_data["username"]
            password = self.validated_data["password"]
            usuario = authenticate(username=username, password=password)
            token, _ = Token.objects.get_or_create(user=usuario)
            return token.key

        return None
