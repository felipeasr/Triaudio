from django import forms
from website.models import teste


class testeForm(forms.ModelForm):
    class Meta:
        model = teste
        fields = ['data_teste', 'tipo_teste', 'orelha_direita_teste', 'orelha_esquerda_teste', 'conduta_teste','observacoes']