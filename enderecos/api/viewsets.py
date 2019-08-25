from rest_framework.viewsets import ModelViewSet

from enderecos.models import ModelEndereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = ModelEndereco.objects.all()
    serializer_class = EnderecoSerializer
