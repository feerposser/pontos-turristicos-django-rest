from rest_framework.serializers import ModelSerializer

from comentarios.models import ModelComentarios


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = ModelComentarios
        fields = ('comentario', 'data', 'aprovado')
