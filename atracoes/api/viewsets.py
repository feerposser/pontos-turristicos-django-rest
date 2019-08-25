from rest_framework.viewsets import ModelViewSet

from atracoes.models import ModelAtracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = ModelAtracao.objects.all()
    serializer_class = AtracaoSerializer
