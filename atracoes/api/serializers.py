from rest_framework.serializers import ModelSerializer

from atracoes.models import ModelAtracao


class AtracaoSerializer(ModelSerializer):

    class Meta:
        model = ModelAtracao
        fields = ('id', 'nome', 'descricao', 'horario_func', 'idade_minima')
