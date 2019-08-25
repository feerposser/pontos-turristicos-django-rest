from django.db import models
from atracoes.models import ModelAtracao
from comentarios.models import ModelComentarios
from avaliacoes.models import ModelAvaliacao
from enderecos.models import ModelEndereco


class ModelPontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(ModelAtracao)
    comentario = models.ManyToManyField(ModelComentarios)
    avaliacao = models.ManyToManyField(ModelAvaliacao, blank=True)
    endereco = models.ForeignKey(ModelEndereco, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='ponto_turistico', blank=True, null=True)

    def __str__(self):
        return self.nome
