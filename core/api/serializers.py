from rest_framework.serializers import ModelSerializer

from core.models import ModelPontoTuristico


class PontoTuristicoSerializer(ModelSerializer):

    class Meta:
        model = ModelPontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',)
