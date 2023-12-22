from django.forms import ModelForm
from .models import Servico, CategoriaManutencao
from equipes.models import Equipe

class FormEquipe(ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})


class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
            

        choices = list()
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.filter(titulo=j).first()
            choices.append((i.value, categoria.get_titulo_display()))
        
        self.fields['categoria_manutencao'].choices = choices