from django import forms
from .models import Categoria, Equipamento

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome',  'descricao']

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao', 'categoria']
