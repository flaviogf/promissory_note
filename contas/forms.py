from django import forms
from contas.models import Conta


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta

        fields = '__all__'

        exclude = ('data_recebimento',)

        widgets = {'contato': forms.HiddenInput()}
