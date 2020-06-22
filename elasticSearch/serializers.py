from rest_framework import serializers
from elasticSearch.models import *


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)


class Car_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Car_datasets

        fields = (
            'document_id', 'price', 'brand', 'model', 'year', 'title_status', 'mileage', 'color', 'vin', 'lot', 'state',
            'country',
            'condition')
