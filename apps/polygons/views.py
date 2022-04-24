from rest_framework import viewsets, status
from rest_framework.permissions import  AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

from .models import Polygon
from .serializers import PolygonSerializer, PolygonDataSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    permission_classes = [AllowAny]

    @action(methods=['GET'], detail=False)
    def descending(self, request):
        """
            RETURN the polygons from the DB, in descending order,
            by number of sides.
            For each polygon include its name and number of sides.

            - Don't import apps.polygons.constants
            - Don't write things like reverse(). Rather, do all the ordering while fetching DB results
        """
        polygon_desended_queryset = Polygon.objects.all().order_by('-num_sides')
        polygon_desended_data = PolygonDataSerializer(polygon_desended_queryset, many=True)
        return Response(polygon_desended_data.data)

    @action(methods=['POST'], detail=False)
    def total_sides(self, request):
        """
            GIVEN a list of polygon names present in field "to_sum",
            RETURN a number, the sum of number of sides for all polygons in the list 
        """
        if request.data.get('to_sum'):
            print(type(request.data.get('to_sum')))
            print(Polygon.objects.filter(name__in=request.data.get('to_sum')))
            sum_data = Polygon.objects.filter(name__in=request.data.get('to_sum')).aggregate(Sum('num_sides'))
            print(sum_data['num_sides__sum'])
            return Response(sum_data['num_sides__sum'])
        else:
            return Response(0)
