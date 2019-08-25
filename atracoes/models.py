from django.db import models


class ModelAtracao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.nome
