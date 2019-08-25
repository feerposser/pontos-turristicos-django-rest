from rest_framework.viewsets import ModelViewSet

from comentarios.models import ModelComentarios
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = ModelComentarios.objects.all()
    serializer_class = ComentarioSerializer
