from rest_framework.serializers import ModelSerializer

from avaliacoes.models import ModelAvaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = ModelAvaliacao
        fields = ('comentario', 'nota', 'data')
