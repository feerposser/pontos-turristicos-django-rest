from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.models import ModelPontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return ModelPontoTuristico.objects.filter(aprovado=True)

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, requuest, pk):
        """
        Em alguns casos as nossas actions(update, destroy....) não são o suficiente para as nossas necessidades
        por isso o django rest framework implementa os actions. Com ele podemos criar uma action personalizada,
        mantendo assim o padrão rest da nossa api.

        Nestre caso vamos simular que um usuário está denunciando um ponto turístico.

        methods = métodos permitidos.
        detail = para usar um recurso (pk). Se detail for false então estaremos utilizando o endpoint inteiro.
        :return:
        """

    # def partial_update(self, request, *args, **kwargs):
    #     """
    #     chamado quando um recurso /1/ patch
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     pass

    # def update(self, request, *args, **kwargs):
    #     """
    #     Chamado quando um recurso /1/ é atualizado (put)
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     """
    #     Chamado quando um recurso (/1/) é solicitado
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     """
    #     Disparado quando um recurso (/1/) DELETE
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     pass

    # def create(self, request, *args, **kwargs):
    #     pass

    # def list(self, request, *args, **kwargs):
    #     """
    #     Método disparado quando e feita uma requisição no endpoint "/pontosturisticos/
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     from rest_framework.response import Response
    #     return Response({"teste": 123})
