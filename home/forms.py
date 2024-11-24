# forms.py
from django import forms
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosGenericos, ArtigosRecommends

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = ArtigoPrincipal  # Use a classe base ArtigoPrincipal como exemplo
        fields = ['titulo', 'texto', 'imagem', 'categories', 'tags']
