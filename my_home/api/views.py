from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from entity.models import Entity

from .serializers import EntitySerializer

ERROR_VALUE_FIELD = 'data[value] должно быть числом!'


class EntityAPIView(APIView):
    def get(self, request):
        entities = Entity.objects.all()
        serializer = EntitySerializer(entities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = self.request.user
        value = request.data['data[value]']
        if not isinstance(value, int) and not isinstance(value, float):
            return Response(
                {'error': ERROR_VALUE_FIELD},
                status=status.HTTP_400_BAD_REQUEST
            )
        entity = Entity.objects.create(modified_by=user, value=value)
        return Response(
            {'entity': model_to_dict(entity)},
            status=status.HTTP_201_CREATED
        )
