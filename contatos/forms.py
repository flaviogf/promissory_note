from django import forms

from contatos.models import Contato, Endereco


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato

        fields = '__all__'

        exclude = ('usuario', )


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco

        fields = '__all__'

        exclude = ('contato', )
