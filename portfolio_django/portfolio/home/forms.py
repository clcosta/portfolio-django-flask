from django import forms
from portfolio.models import Projeto


class ProjetoCreateForm(forms.ModelForm):
    
    titulo = forms.CharField(
        label="Titulo do Projeto",
		max_length = 100,
        required=True,
        min_length=5,
	)

    capa = forms.FileField(
        label= "Selecione uma imagem para a Capa do Projeto",
        allow_empty_file=False,
        required=True,
    )

    link_codigo = forms.URLField(
        label= "link do Código no GitHub ",
        required=True,
    )

    iframe_video = forms.CharField(
        label = "Iframe (Vídeo) que será exibido na página! ",
        max_length=1000,
        widget=forms.widgets.Textarea,
    )

    class Meta:
        model = Projeto
        fields = '__all__'
