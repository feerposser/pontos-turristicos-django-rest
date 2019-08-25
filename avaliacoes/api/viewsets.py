from rest_framework.viewsets import ModelViewSet

from avaliacoes.models import ModelAvaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = ModelAvaliacao.objects.all()
    serializer_class = AvaliacaoSerializer