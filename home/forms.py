from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'texto', 'imagem', 'categories', 'tags', 'tipo']

    # Opcional: Personalizar rótulos ou widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].widget = forms.Select(choices=Artigo.TIPO_CHOICES)
        self.fields['tipo'].label = "Tipo de Artigo"
