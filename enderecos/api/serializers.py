from rest_framework.serializers import ModelSerializer

from enderecos.models import ModelEndereco


class EnderecoSerializer(ModelSerializer):

    class Meta:
        model = ModelEndereco
        fields = ('id', 'linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longitude',)
