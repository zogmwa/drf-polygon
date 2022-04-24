from rest_framework import serializers

from .models import Polygon


class PolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polygon
        fields = '__all__'
        write_only_fields = ('id',)

class PolygonDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polygon
        fields = [
            'name',
            'num_sides'
        ]
