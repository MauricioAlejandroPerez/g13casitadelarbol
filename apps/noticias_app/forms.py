from django import forms
from .models import Comentarios, Noticia



class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = ('autor', 'titulo', 'contenido', 'categorias')

        widgets = {
            "titulo": forms.TextInput(attrs={'class':'TextInputClass'}),
            "contenido": forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('cuerpo_comentario',)

        widgets = {
            'cuerpo_comentario' : forms.Textarea(attrs={'class':'form-control'}),
        }